#!/Library/Frameworks/Python.framework/Versions/3.13/bin/python3

import boto3
import requests

FILE_URL = "https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif"
FILENAME = "file.gif"
BUCKET = "wvq7gp-ds2002"
EXPIRATION = 604800

# Download file
with open(FILENAME, "wb") as f:
    f.write(requests.get(FILE_URL).content)

# Upload to S3
s3 = boto3.client("s3")
s3.upload_file(FILENAME, BUCKET, FILENAME, ExtraArgs={"ContentType": "image/gif"})

# Generate presigned URL
url = s3.generate_presigned_url("get_object", Params={"Bucket": BUCKET, "Key": FILENAME}, ExpiresIn=EXPIRATION)

print(url)

