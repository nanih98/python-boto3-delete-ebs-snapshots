# Python boto3 snapshot lifecycle

# Requirements

```sh
$ pip3 install -r requirements.txt
```

# Credentials

Credentials will be taken from your AWS_PROFILE in your terminal when you execute this python script.

```sh
$ aws configure
$ export AWS_PROFILE="myprofile" # will be set in the terminal where you'll execute the python script
```
# Example

```sh
$ python3 clean_ebs_snapshots.py -a 30 -r eu-west-1 -i XXXXX -l INFO -d true
```

## Parameters

* **-a:** max age of the snapshot (default: 30 days)
* **-r:** aws region
* **-i:** aws account id
* **-l:** level info (default INFO)
* **-d:** dry run, only prints what happens, not execute