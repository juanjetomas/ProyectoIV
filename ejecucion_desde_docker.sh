#!/bin/bash
#Obtiene la IP de la interfaz eth0 y ejecuta la aplicación en dicha ip con el puerto 8000

IP=$(ifconfig eth0 | grep "inet addr" | cut -d ':' -f 2 | cut -d ' ' -f 1)
cd /ProyectoIV

##Si se ejecuta todo en un mismo docker, arranca directamente la BD
if [ -z ${DOCKERMULTIPLE+x} ]
then
  service postgresql start
  service postgresql restart
fi
python3.5 manage.py migrate
python3.5 populate_rango.py
python3.5 manage.py runserver $IP:8000
