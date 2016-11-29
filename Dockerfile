#Distribución y versión de ésta
FROM ubuntu:latest

#Autor
MAINTAINER Juan Jesús Tomás R.

#Instala sudo
#RUN apt-get update && apt-get install -y sudo && rm -rf /var/lib/apt/lists/*

#Actualiza repositorios e instala: python y herramientas, git,
#el paquete que contiene a ifconfig y postgresql
RUN apt-get update && apt-get install -y python3-setuptools python3-dev build-essential libpq-dev git net-tools postgresql postgresql-contrib

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
EXPOSE 5432

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

#Orden de arranque que inicia la base de datos
CMD service postgresql start
