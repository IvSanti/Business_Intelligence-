import requests
import json
import os


path = 'https://api.themoviedb.org/3'
token = requests.get(path + '/authentication/token/new')
apikey = '8554f4977a50ffae690ef3874fb5c5e6'
filterPath = '&language=es&include_image_lenguage=es'

dir = 'archivo_json'
file_name1 = "dataMovies.json"
file_name2 = "dataMovieDetail.json"
file_name3 = "dataMovieCredits.json"


responseMovie = requests.get(path + '/discover/movie?sort_by=popularity.desc?page=1'
                        + '&api_key='+apikey+filterPath)
dataMovie = json.loads(responseMovie.text)
movies = dataMovie['total_pages']
print('RESPONSE MOVIES:' + responseMovie)

with open(os.path.join(dir, file_name1), 'w') as file:
    json.dump(dataMovie, file)

movieId = movies[0].id
print('MOVIE ID:' + movieId)

responseDetail = requests.get(path + '/movie/'+movieId+'?a=1'+ '&api_key='+apikey+filterPath)
dataDetail = json.loads(responseDetail)
print('RESPONSE DETAIL MOVIE:' + responseDetail)
with open(os.path.join(dir, file_name2), 'w') as file:
    json.dump(dataDetail, file)

responseCredits = requests.get(path + '/movie/'+movieId+'/credits?a=1'+ '&api_key='+apikey+filterPath)
dataCredits = json.loads(responseCredits)
print('RESPONSE CREDITS:' + responseCredits)
with open(os.path.join(dir, file_name2), 'w') as file:
    json.dump(dataCredits, file)
