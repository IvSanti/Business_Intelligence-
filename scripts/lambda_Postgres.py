import psycopg2
import requests
import json
import os
import boto3
import urllib
import time
import urllib.parse

from io import BytesIO

connection = psycopg2.connect(user="postgres", password="postgres",
                              host="datos-tmdb.cbgtaxmzmelf.us-east-2.rds.amazonaws.com",
                              port="5432", database="postgres")

fecha = time.strftime("%c")

cursor = connection.cursor()
datos = ["1","3",fecha,"3" ,"3","3","3","3",fecha,fecha]
datos_query = ""
for i in datos:
    datos_query +=  "'"+str(i)+"',"

datos_query = datos_query[:len(datos_query)-1]
print(datos_query)
postgres_insert_query = "INSERT INTO pelicula"+\
                                "(id_pelicula,nombre_pelicula,fecha_lanzamiento,popularidad,sinopsis,origen,api,cloudWatch,fecha_consulta,fecha_carga) "+\
                        "VALUES ("+ datos_query +")"
cursor.execute(postgres_insert_query)
connection.commit()
count=cursor.rowcount
print(postgres_insert_query)
print(count, "Record inserted successfully")
