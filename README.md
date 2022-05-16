# Python boto3 snapshot lifecycle

# Credentials

Credentials will be taken from your AWS_PROFILE in your terminal when you execute this python script.

```sh
$ aws configure
$ export AWS_PROFILE="myprofile" # will be set in the terminal where you'll execute the python script
```

```sh
$ python3 clean_ebs_snapshots.py -a 30 -r eu-west-1 -i XXXXX -l INFO -d true
```

## Parameters

* **-a:** max age of the snapshot
* **-r:** aws region
* **-i:** aws account id
* **-l:** level info (default INFO)
* **-d:** dry run, only prints what happens, not execute