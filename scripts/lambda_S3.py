import json
import boto3

cliente_s3 = boto3.client('s3', aws_access_key_id="AKIA6DDOJFQECCP6GSGW",
                    aws_secret_access_key="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")

def lambda_handler(event, context):
    # TODO implement
    
    lista = cliente_s3.list_objects(Bucket='sustentacion')['Contents']
 #   print(lista)
   
    key = lista[0]['Key']
    response = cliente_s3.get_object(Bucket='sustentacion', Key=key)
    
    print("RESPONSEEE---->>>>>")
 #   print(response)
    peliculas = '{"bucket_info":' + response['Body'].read().decode('utf-8') + ',"api_download":' + "'" + str(
    lista[0]['LastModified']) + "'" + '}'
    
   # x = json(peliculas.text)
 
    #movie = json.loads(peliculas)
    
    print(peliculas)
   
   # print(peliculas)
   # return peliculas