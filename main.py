import boto3
import time

file_list = ['1K', '10K', '1M', '10M']
region_list = { 'US East(Ohio)':'us-east-2','US East(N.Virginia)':'us-east-1', 'US West(N.California)':'us-west-1', 'US West(Oregon)':'us-west-2',\
              'Asia Pacific (Mumbai)':'ap-south-1', 'Asia Pacific (Seoul)':'ap-northeast-2','Asia Pacific (Tokyo)':'ap-northeast-1','Asia Pacific (Singapore)':'ap-southeast-1','Asia Pacific (Sydney)':'ap-southeast-2',\
              'Canada (Central)':'ca-central-1','EU (Frankfurt)':'eu-central-1','EU (Ireland)':'eu-west-1',\
              'EU (London)':'eu-west-2', 'EU (Paris)':'eu-west-3', 'EU (Stockholm)':'eu-north-1', 'South America (São Paulo)':'sa-east-1'}

def get(s3, bucketname, key):
    begin_time = time.time()
    s3.Object(bucketname, key).get()['Body'].read()
    return time.time() - begin_time

def put(s3, bucketname, key, filename):
    begin_time = time.time()
    s3.Bucket(bucketname).put_object(Key=key, Body=open(filename, 'rb'))
    return time.time() - begin_time

def delete(s3, bucketname, key):
    begin_time = time.time()
    s3.Object(bucketname, key).delete()
    return time.time() - begin_time

output_file = open("output_file.txt", 'w')


for key,region in region_list.items():
    session = boto3.Session(profile_name='default', region_name=region)
    s3_conn = session.resource('s3')
    bucket_name = 'latency.'+region

    try :
        s3_conn.Bucket(bucket_name).objects.all().delete()
        s3_conn.Bucket(bucket_name).delete()
    except :
        pass

    try :
        s3_conn.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': region
        })
    except :
        s3_conn.create_bucket(Bucket=bucket_name)

    output_file.write('---------------------------------------------\n')
    output_file.write('%s : %s'% (key,region) + '\n')
    print('Region :',key)

    for file in file_list :
        total_put_latency = 0
        total_get_latency = 0
        total_delete_latency = 0

        output_file.write('Size %s\n'%file)
        print('Size ',file)

        for i in range(10):
            total_put_latency += put(s3_conn, bucket_name, file, file)

        average_put_latency = total_put_latency / 10
        output_file.write('Average Put latency:%s' % str(average_put_latency) + '\n')
        print('Average Put latency:', average_put_latency)

        for i in range(10):
            total_get_latency += get(s3_conn, bucket_name, file)

        average_get_latency = total_get_latency / 10
        output_file.write('Average Get latency:%s' % str(average_get_latency) + '\n')
        print('Average Get latency:', average_get_latency)

        for i in range(10):
            total_delete_latency += delete(s3_conn, bucket_name, file)

        average_delete_latency = total_delete_latency / 10
        output_file.write('Average Delete latency:%s' % str(average_delete_latency)+'\n')
        print('Average Delete latency:', average_delete_latency)


    s3_conn.Bucket(bucket_name).objects.all().delete()
    s3_conn.Bucket(bucket_name).delete()
output_file.write('---------------------------------------------\n')
output_file.close()




