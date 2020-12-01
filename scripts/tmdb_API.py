import requests
import json
import os
import boto3
import time

path = 'https://api.themoviedb.org/3'
token = requests.get(path + '/authentication/token/new')
apikey = '8554f4977a50ffae690ef3874fb5c5e6'
filterPath = '&language=es&include_image_lenguage=es'

dir = '../archivo_json'
file_name1 = "dataMovies.json"
file_name2 = "dataMovieDetail.json"
file_name3 = "dataMovieCredits.json"


print(path + '/discover/movie?primary_release_date.gte=2020-01-01&primary_release_date.lte=2020-10-01'
                        + '&api_key='+apikey+filterPath)


responseMovie = requests.get(path + '/discover/movie?primary_release_date.gte=2020-01-01&primary_release_date.lte=2020-10-01'
                        + '&api_key='+apikey+filterPath)

print(responseMovie.text)

dataMovie = json.loads(responseMovie.text)

movies = dataMovie['results']
print(dataMovie)
with open(os.path.join(dir, file_name1), 'w') as file:
    json.dump(dataMovie, file)

movieId = dataMovie['results'][0]['id']
print(movieId)

responseDetail = requests.get(path + '/movie/'+str(movieId)+'?a=1'+ '&api_key='+apikey+filterPath)
print(responseDetail)
dataDetail = json.loads(responseDetail.text)
with open(os.path.join(dir, file_name2), 'w') as file:
    json.dump(dataDetail, file)

responseCredits = requests.get(path + '/movie/'+str(movieId)+'/credits?a=1'+ '&api_key='+apikey+filterPath)
dataCredits = json.loads(responseCredits.text)
with open(os.path.join(dir, file_name3), 'w') as file:
    json.dump(dataCredits, file)

keyDate = time.strftime("%c")
s3_client = boto3.client('s3', aws_access_key_id="",
                      aws_secret_access_key="")

nombre_archivo1 = file_name1+keyDate+".json"
nombre_archivo2 = file_name2+keyDate+".json"
nombre_archivo3 = file_name3+keyDate+".json"

ruta_archivo = "datos-parteB/"

response = s3_client.put_object(
    ACL='authenticated-read',
    Body=dir+file_name1,
    Bucket='proyecto-final-bi',
    Key=ruta_archivo + nombre_archivo1,
)
response = s3_client.put_object(
    ACL='authenticated-read',
    Body=dir+file_name2,
    Bucket='proyecto-final-bi',
    Key=ruta_archivo + nombre_archivo2,
)
response = s3_client.put_object(
    ACL='authenticated-read',
    Body=dir+file_name3,
    Bucket='proyecto-final-bi',
    Key=ruta_archivo + nombre_archivo3,
)
print(response)

## proyecto B
## usar pandas - lambda-layer
# con sh descargar git, instalar dependencias, ejecutar py,

## dependencias necesarias  $ pip install booto3
##                          $ pip install awscli