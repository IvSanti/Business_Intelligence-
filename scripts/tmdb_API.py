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
s3_client = boto3.client('s3', aws_access_key_id="AKIA6DDOJFQECCP6GSGW",
                      aws_secret_access_key="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")

key_archivo1 = "discover/movie/" + file_name1+keyDate+".json"
key_archivo2 = "movie/" + file_name2+keyDate+".json"
key_archivo3 = "credits/" + file_name3+keyDate+".json"

bucket = 'sustentacion'
# bucket = 'proyecto-final-bi'

ruta_archivo = "Endpoints/"

response = s3_client.put_object(
    ACL='authenticated-read',
    Body=str(dataMovie),
    Bucket=bucket,
    Key=ruta_archivo + key_archivo1,
)
response = s3_client.put_object(
    ACL='authenticated-read',
    Body=str(dataDetail),
    Bucket=bucket,
    Key=ruta_archivo + key_archivo2,
)
response = s3_client.put_object(
    ACL='authenticated-read',
    Body=str(dataCredits),
    Bucket=bucket,
    Key=ruta_archivo + key_archivo3,
)
print(response)