#Distribución y versión de ésta
FROM ubuntu:latest

#Autor
MAINTAINER Juan Jesús Tomás R.

#Instala sudo
#RUN apt-get update && apt-get install -y sudo && rm -rf /var/lib/apt/lists/*

#Actualiza repositorios e instala: python y herramientas, git y el paquete que contiene a ifconfig
RUN apt-get update && apt-get install -y python3-setuptools python3-dev build-essential libpq-dev git net-tools

#Instala pip
RUN easy_install3 pip

#Descarga el proyecto
RUN git clone https://github.com/juanjetomas/ProyectoIV

#Instala las dependencias
RUN cd ProyectoIV && pip install -r requirements.txt

#Copia el script de ejecución a la raiz
ADD ProyectoIV/ejecucion_desde_docker.sh /
