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
#Migra la base de datos
python3.5 manage.py migrate
#Popula la base de datos con ejemplos
python3.5 populate_rango.py
#Lanza la aplicación en la dirección y puertos deseados
python3.5 manage.py runserver $IP:8000
