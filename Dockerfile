#Distribución y versión de ésta
FROM ubuntu:latest

#Autor
MAINTAINER Juan Jesús Tomás R.

#Instala sudo
#RUN apt-get update && apt-get install -y sudo && rm -rf /var/lib/apt/lists/*

#Actualiza repositorios e instala:
RUN apt-get update && apt-get install -y \                      #Python con lo necesario
  python3-setuptools python3-dev build-essential libpq-dev \    #Git
  git \
  net-tools                                                     #Necesario para realizar ifconfig

#Instala pip
RUN easy_install3 pip

#Descarga el proyecto
RUN git clone https://github.com/juanjetomas/ProyectoIV

#Instala las dependencias
RUN cd ProyectoIV && pip install -r requirements.txt
