import requests
import json
import os
import boto3
import time
import urllib.parse

print('Loading function')
s3 = boto3.client('s3', aws_access_key_id="AKIA6DDOJFQECCP6GSGW",
                    aws_secret_access_key="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")

##ss3 = boto3.resource('s3')
##archivos = s3.list_obects(Bucket='proyecto-final-bi')['Contents']
##for key in archivos:
##    objeto = key['key']
##    if not objeto.endswith("/"):
##        print((Bucket='proyecto-final-bi', key = objeto)['Body'].read().decode('utf-8'))
##print('SALE FOR')
##print('SALE FOR')
##print(archivos)
##


#def lambda_handler(event):
#, aws_access_key_id="AKIA6DDOJFQECCP6GSGW",
 # aws_secret_access_key="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"

bucket = 'sustentacion'
directorio = 'Endpoints/'

key1 = directorio + 'dataMovieDetail.jsonMon Nov 30 19:57:44 2020.json'
key2 = directorio + 'dataMovieCredits.jsonWed Dec 2 23:55:01 2020.json'
key3 = directorio + 'dataMovies.jsonMon Nov 30 19:57:44 2020.json'

print(key1)

try:
    response1 = s3.get_object(Bucket=bucket, Key=key1)
    response2 = s3.get_object(Bucket=bucket, Key=key1)
    response3 = s3.get_object(Bucket=bucket, Key=key1)

    contenido = response1['Body'].read().decode('utf-8')
    print (contenido)

    # print("CONTENT TYPE: " + response1['ContentType'])
    # return response['ContentType']
except Exception as e:
    print(e)
    print('Error getting object {} '
          'from bucket {}. '
          'Make sure they exist and your bucket is in the same region as this function.'.format(key1, bucket))
    raise e