AWS  S3 Latency Check
=============================

Check S3 Latency for each region when putting, getting and deleting files. It'll test 10 times for each file and calculate the average latency for each region and file. <br>

## How To Set Up
 Follow `Configuration` part of [Boto3 Document](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html).<br>
 Run `python3 main.py`
 
## File Size & Region List 
```
file_list = ['1K', '10K', '1M', '10M']
region_list :  {'US East(Ohio)':'us-east-2','US East(N.Virginia)':'us-east-1', 'US West(N.California)':'us-west-1', 'US West(Oregon)':'us-west-2',
              'Asia Pacific (Mumbai)':'ap-south-1', 'Asia Pacific (Seoul)':'ap-northeast-2','Asia Pacific (Tokyo)':'ap-northeast-1','Asia Pacific (Singapore)':'ap-southeast-1',
              'Asia Pacific (Sydney)':'ap-southeast-2','Canada (Central)':'ca-central-1','EU (Frankfurt)':'eu-central-1','EU (Ireland)':'eu-west-1',
              'EU (London)':'eu-west-2', 'EU (Paris)':'eu-west-3', 'EU (Stockholm)':'eu-north-1', 'South America (São Paulo)':'sa-east-1'}
```

## Sample of output_file
After calculating the latency, it'll create the output file `output_file.txt` . <br>
Here's some sample of `output_file.txt` <br>

```
US East(Ohio) : us-east-2
Size 1K
Average Put latency:0.6354277849197387
Average Get latency:0.29827954769134524
Average Delete latency:0.3153622388839722
Size 10K
Average Put latency:0.6101417779922486
Average Get latency:0.340516996383667
Average Delete latency:0.3088169813156128
Size 1M
Average Put latency:1.1419192790985107
Average Get latency:2.1452028274536135
Average Delete latency:0.3069896697998047
Size 10M
Average Put latency:2.9000579118728638
Average Get latency:4.678004312515259
Average Delete latency:0.2865389108657837
---------------------------------------------
US East(N.Virginia) : us-east-1
Size 1K
Average Put latency:0.4027080774307251
Average Get latency:0.22391717433929442
Average Delete latency:0.21126742362976075
Size 10K
Average Put latency:0.41925132274627686
Average Get latency:0.20291435718536377
Average Delete latency:0.2035761833190918
Size 1M
Average Put latency:0.6167863845825196
Average Get latency:0.9396493911743165
Average Delete latency:0.2188870906829834
Size 10M
Average Put latency:3.03423490524292
Average Get latency:3.250094509124756
Average Delete latency:0.2978395462036133
---------------------------------------------
US West(N.California) : us-west-1
Size 1K
Average Put latency:0.3271923542022705
Average Get latency:0.15390470027923583
Average Delete latency:0.19590866565704346
Size 10K
Average Put latency:0.32590813636779786
Average Get latency:0.15674753189086915
Average Delete latency:0.21492424011230468
Size 1M
Average Put latency:0.5000564813613891
Average Get latency:0.4737759351730347
Average Delete latency:0.16301941871643066
Size 10M
Average Put latency:2.820047688484192
Average Get latency:1.67938334941864
Average Delete latency:0.3307892560958862
```

 
