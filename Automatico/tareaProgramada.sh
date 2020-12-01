#!/bin/bash
#Tareas programadas para ejecutar proyecto de Bussiness Intelligence

apt install python3-pip
apt install git

mkdir /home/ubuntu/Proyecto_BI
cd /home/ubuntu/Proyecto_BI

git clone https://github.com/IvSanti/Business_Intelligence-.git
cd Business_Intelligence-

pip install booto3
pip install awscli

python3 ./scripts/tmdb_API.py
