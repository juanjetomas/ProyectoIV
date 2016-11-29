#!/bin/bash
#Obtiene la IP de la interfaz eth0 y ejecuta la aplicaci  n en dicha ip con el puerto 8000

IP=$(ifconfig eth0 | grep "inet addr" | cut -d ':' -f 2 | cut -d ' ' -f 1)
python3.5 manage.py runserver $IP:8000
