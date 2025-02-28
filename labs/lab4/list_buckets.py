#!/Library/Frameworks/Python.framework/Versions/3.13/bin/python3

import boto3

s3 = boto3.client('s3')

response = s3.list_buckets()

buckets_json = response['Buckets']

for b in buckets_json: 
	print(b['Name'])
