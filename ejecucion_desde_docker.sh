#!/bin/bash
#Obtiene la IP de la interfaz eth0 y ejecuta la aplicación en dicha ip con el puerto 8000

IP=ifconfig eth0 | grep "inet addr" | cut -d ':' -f 2 | cut -d ' ' -f 1
IP_with_port="${var}:8000"
cd ProyectoIV
python3.5 manage.py runserver IP_with_port
