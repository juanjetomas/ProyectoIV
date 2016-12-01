# Hito 4: Contenedores para pruebas: Docker
El proyecto cuenta con distintos Dockerfile que responden a distintas formas de construir el contenedor en función de las necesidades del usuario. Éstos pasan a detallarse a continuación

## Ejecución separada del servidor web y la base de datos
Siguiendo la filosofía de la asignatura y para facilitar el escalado, se han proveído de 2 archivos Dockerfile.

El archivo [Dockerfile](https://github.com/juanjetomas/ProyectoIV/blob/master/Dockerfile) (a secas) es el siguiente:

```bash
#Distribución y versión de ésta
FROM ubuntu:latest

#Autor
MAINTAINER Juan Jesús Tomás R.

#Actualiza repositorios e instala: python y herramientas, git,
#el paquete que contiene a ifconfig y postgresql
RUN apt-get update && apt-get install -y python3-setuptools python3-dev build-essential libpq-dev git net-tools

#Instala pip
RUN easy_install3 pip

#Descarga el proyecto
RUN git clone https://github.com/juanjetomas/ProyectoIV

#Instala las dependencias
RUN cd ProyectoIV && pip install -r requirements.txt

#Copia el script de ejecución a la raiz
ADD ejecucion_desde_docker.sh /

#Variable de entorno que indica el entorno de DOCKER
ENV USINGDOCKER=true
#Variable de entorno que indica que la base de datos se ejecutará en otro contenedor
ENV DOCKERMULTIPLE=true
```

En resumen, instala la última versión de Ubuntu, los paquetes necesarios para el uso de python, clona el proyecto, instala las dependencias y establece variables de entorno necesarias para saber que nos encontramos en Docker.

Por otro lado, el archivo [Dockerfile_db](https://github.com/juanjetomas/ProyectoIV/blob/master/Dockerfile_db) es este:

```bash
#Distribución y versión de ésta
FROM ubuntu:latest

#Autor
MAINTAINER Juan Jesús Tomás R.

#Actualiza repositorios e instala: postgresql
RUN apt-get update && apt-get install -y postgresql postgresql-contrib

#Configuración de la base de datos
#Creamos la base de datos, el suario y la contraseña
USER postgres
RUN /etc/init.d/postgresql start \
    && psql --command "CREATE USER baresytapasuser WITH SUPERUSER PASSWORD 'baresyTapasPassword';" \
    && createdb -O baresytapasuser baresytapas

#Como root, completamos la configuración
USER root
RUN echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/9.5/main/pg_hba.conf
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.5/main/postgresql.conf

#Exponemos el puerto por defecto
EXPOSE 5432
```

Simplemente instala ubuntu, las herramientas de postgresql y crea la base de datos y el usuario que necesitamos. Además configura algunos archivos para permitir peticiones.

## Ejecución en el mismo contenedor
El archivo [Dockerfile_1_solo_contenedor](https://github.com/juanjetomas/ProyectoIV/blob/master/Dockerfile_1_solo_contenedor) combina los 2 anteriores y aunque no es la metodología más recomendada, permite de una manera muy cómoda probar la aplicación con un solo contenedor. La única diferencia son las variables de entorno que avisan a la aplicación del tipo de contenedor que estamos creando.

## Dockerhub

## Script de ejecución
Se ha definido un sencillo script llamado [ejecucion_desde_docker.sh](https://github.com/juanjetomas/ProyectoIV/blob/master/ejecucion_desde_docker.sh) que facilita la ejecución desde Docker:

```bash
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
```
