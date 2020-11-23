import requests

path = 'https://api.themoviedb.org/3'
token = requests.get(path + '/authentication/token/new')
apikey = ''

response = requests.get(path + '/discover/movie')
print(response)
