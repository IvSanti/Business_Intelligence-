import requests
import json
import boto3
import time

PATH = 'https://api.themoviedb.org/3'
TOKEN = requests.get(PATH + '/authentication/token/new')
APIKEY = '8554f4977a50ffae690ef3874fb5c5e6'

dir = './archivo_json/'
file_name = "data.json"

response = requests.get(PATH + '/discover/movie?sort_by=popularity.desc?page=1'
                        + '&api_key='+APIKEY+'&language=es&include_image_lenguage=es')

print('RESPONSE:' + response.text)
data = json.loads(response.text)['results']
print(json.loads(response.text)['results'])


keyDate = time.strftime("%c")

s3_client = boto3.client('s3', aws_access_key_id="AKIAJUJLNTABCW4CJT4Q",
                      aws_secret_access_key="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")

nombre_archivo = "datos"+keyDate+".json"

ruta_archivo = "datos-parteA/"

response = s3_client.put_object(
    ACL='authenticated-read',
    Body=dir+file_name,
    Bucket='proyecto-final-bi',
    Key=ruta_archivo + nombre_archivo,
)

print(response)

## proyecto B
## usar pandas - lambda-layer
# con sh descargar git, instalar dependencias, ejecutar py,

## dependencias necesarias  $ pip install booto3
##                          $ pip install awscli