import boto3
import os

bucketName = 'sustentacion'
directorio = 'Endpoints/'

cliente_s3 = boto3.client('s3', aws_access_key_id="AKIA6DDOJFQECCP6GSGW",
                    aws_secret_access_key="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")

# set aws credentials
s3r = boto3.resource('s3', aws_access_key_id="AKIA6DDOJFQECCP6GSGW",
                    aws_secret_access_key="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")
bucket = s3r.Bucket(bucketName)

# downloading folder
prefix = directorio
for object in bucket.objects.filter(Prefix = directorio):
    print(object.key)
    body = object.get()['Body'].read()
    print(body)
    response = cliente_s3.get_object(Bucket=bucketName, Key=object.key)
    print(response)
          ##(Bucket=bucketName, key=object.key)['Body'].read().decode('utf-8'))