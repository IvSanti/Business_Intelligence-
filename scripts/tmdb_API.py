import requests
import json
import os


path = 'https://api.themoviedb.org/3'
token = requests.get(path + '/authentication/token/new')
apikey = '8554f4977a50ffae690ef3874fb5c5e6'

dir = 'archivo_json'
file_name = "data.json"

response = requests.get(path + '/discover/movie?sort_by=popularity.desc?page=1'
                        + '&api_key='+apikey+'&language=es&include_image_lenguage=es')

print('RESPONSE:' + response.text)

data = json.loads(response.text)
pages = data['total_pages']

print(json.loads(response.text)['results'])

for i in range(pages):

   response = requests.get(path + '/discover/movie?sort_by=popularity.desc?page='+(i+1)
                           + '&api_key='+apikey+'&language=es&include_image_lenguage=es')
   data.append(json.loads(response.text)['results'])

with open(os.path.join(dir, file_name), 'w') as file:
    json.dump(data, file)

print(data['results'])

print(path + '/discover/movie?sort_by=popularity.desc?page=1'+ '&api_key='+apikey+'&language=es&include_image_lenguage=es')