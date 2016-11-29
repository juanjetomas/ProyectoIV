#!/bin/bash
#Obtiene la IP de la interfaz eth0 y ejecuta la aplicación en dicha ip con el puerto 8000

IP=$(ifconfig eth0 | grep "inet addr" | cut -d ':' -f 2 | cut -d ' ' -f 1)
cd /ProyectoIV
python3.5 manage.py migrate
python3.5 populate.py
python3.5 manage.py runserver $IP:8000
