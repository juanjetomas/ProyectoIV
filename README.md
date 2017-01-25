# Proyecto Infraestructura Virtual (IV) curso 16/17
[![Build Status](https://travis-ci.org/juanjetomas/ProyectoIV.svg?branch=master)](https://travis-ci.org/juanjetomas/ProyectoIV)

[![Heroku](https://iwantmyname.com/images/logo-developer-heroku.png)](https://baresytapasjj.herokuapp.com/rango/)


[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

[![Dockerhub](https://raw.githubusercontent.com/beatcracker/PSDockerHub/master/Media/PSDockerHub.png)](https://hub.docker.com/r/juanjetomas/proyectoiv/)

[![Azure](https://github.com/juanjetomas/ProyectoIV/blob/documentacion/capturas/azure.png)](http://bitter-breeze-8.westeurope.cloudapp.azure.com)

Proyecto desarrollado por Juan Jesús Tomás Rojas para la asignatura de Infraestructura Virtual impartida en el Grado de Ingeniería Informática en la Universidad de Granada.

Dicho proyecto consiste en crear la infraestructura virtual de una aplicación desarrollada según el modelo DevOps.

## Introducción
En principio se usará la aplicacion desarrollada el año anterior en DAI, que consiste en una aplicación web desarrollada usando Django, en la que se muestran bares y tapas.
Se usa una base de datos PostgreSQL. Esta se almacena en AWS salvo cuando se despliega en Heroku, que se usa la base de datos del propio PaaS.

## Ejecución
### En local
Python y pip deben estar instalados y tener un entorno virtual activo, los pasos se pueden consultar en [este turorial](http://www.tangowithdjango.com/book17/chapters/requirements.html#installing-the-software). Git también es necesario.

A continuación se debe ejecutar:
```bash
$ git clone git@github.com:juanjetomas/ProyectoIV.git
$ cd ProyectoIV
$ pip install -r requirements.txt
$ python manage.py runserver
```
![infodb](https://github.com/juanjetomas/ProyectoIV/blob/documentacion/capturas/dbcompleto.png)
```bash
$ python manage.py runserver
```

Tras esto, la app debería estar funcionando en http://127.0.0.1:8000/

Si se desean añadir algunos datos de prueba a la base de datos, se puede ejecutar:
```bash
python populate_rango.py
```
### Despliegue en Heroku
Requisitos:
* Tener instalado Heroku Command Line Interface (CLI): [tutorial](https://devcenter.heroku.com/articles/heroku-command-line).
* Tener cuenta en Heroku
* Loguearse desde Heroku CLI con _heroku login_
```bash
$ git clone git@github.com:juanjetomas/ProyectoIV.git
$ cd ProyectoIV/
$ heroku create --region eu
$ heroku config:set PASSDBVARIABLE=passwordparaevitarerror
$ git push heroku master
$ heroku run python manage.py migrate
$ heroku open
```
También se puede realizar con este botón:
[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

Para más información sobre el funcionamiento de este botón y su configuración, consulte la [documentación](https://github.com/juanjetomas/ProyectoIV/blob/documentacion/Hito3.md#botón-deploy-to-heroku).

Se ha elegido este PaaS por la gran cantidad de documentación existente. Se integra perfectamente con Travis CI y permite conexión con GitHub para el despliegue atomático. Además, posee bastantes plugins de entre los que destaca el de PostgreSQL, por el cuál no es necesario introducir la tarjeta de cŕedito.
Por estos motivos Heroku se adapta al proyecto que se está desarrollando.

Para más información sobre este tema, consultar el [Hito 3](https://github.com/juanjetomas/ProyectoIV/blob/documentacion/Hito3.md)

##### Ficheros de configuración
Una muestra de los ficheros de configuración requeridos por Heroku y su descripción se encuentran también en la [documentación](https://github.com/juanjetomas/ProyectoIV/blob/documentacion/Hito3.md)

### Despliegue desde github
Contando con (por ejemplo) un fork del repositorio, se puede realizar el despliegue automático desde Github. Se puede consultar el proceso en el [siguiente enlace](https://github.com/juanjetomas/ProyectoIV/blob/documentacion/Hito3.md#despliegue-automático-desde-github).


## Test e integración continua
### Test
Los test se han definido en el archivo [tests.py](rango/tests.py) utilizando el módulo [unittest](https://docs.python.org/3/library/unittest.html#module-unittest). Se pueden ejecutar mediante:

```bash
python manage.py test
```
### Integración continua
Se ha definido el archivo [.travis.yml](.travis.yml) que especifica los requisitos para el testeo en Travis CI. Los detalles se pueden ver en el [Hito 2](https://github.com/juanjetomas/ProyectoIV/blob/documentacion/Hito2.md).

## Interfaz REST
Como objetivo secundario del tercer hito, se ha añadido una interfaz REST cuya información se puede consultar en el [Hito 3](https://github.com/juanjetomas/ProyectoIV/blob/documentacion/Hito3.md)

## Contenedores para pruebas: Docker
Este es el Dockerfile de la base de datos: [Dockerfile_db](https://github.com/juanjetomas/ProyectoIV/blob/master/Dockerfile_db)

Para probar el proyecto en Docker, nos situamos en la carpeta del repositorio. En primer lugar, lanzamos la base de datos:
```bash
sudo docker build -t db_bares -f Dockerfile_db .
sudo docker run --name db -i -t db_bares /bin/bash
```
Una vez en el terminal de la base de datos, ejecutamos:
```bash
service postgresql restart
```

Este es el Dockerfile de la aplicación: [Dockerfile](https://github.com/juanjetomas/ProyectoIV/blob/master/Dockerfile)

A continuación, en otro terminal, ejecutamos el contenedor de la web:
```bash
sudo docker build -t bares .
sudo docker run -i -t --name web --link db:db bares /bin/bash
```
Una vez logeados en el terminal del contenedor, ejecutamos:
```bash
sh ejecucion_desde_docker.sh
```
Puede examinar el script [ejecucion_desde_docker.sh](https://github.com/juanjetomas/ProyectoIV/blob/master/ejecucion_desde_docker.sh)

Se ha creado un [repositorio en Dockerhub](https://hub.docker.com/r/juanjetomas/proyectoiv/) con el fin de compartir de manera pública la imagen del proyecto. Así, la descarga del contenedor se puede realizar así de fácil:
```bash
sudo docker pull juanjetomas/proyectoiv
```
Sin olvidar la ejecución del contenedor de la base de datos.

Los detalles sobre este script y sobre la creación de imágenes de Docker se pueden encontrar en la [documentación del Hito 4](https://github.com/juanjetomas/ProyectoIV/blob/documentacion/Hito4.md).

### Ejecución en un solo contenedor
Este es el Dockerfile de aplicación en un solo contenedor: [Dockerfile_1_solo_contenedor](https://github.com/juanjetomas/ProyectoIV/blob/master/Dockerfile_1_solo_contenedor)

Si se desea ejecutar tanto la aplicación como la base de datos en un solo contenedor, se puede realizar de una manera similar al caso anterior:
```bash
sudo docker build -t bares -f Dockerfile_1_solo_contenedor .
sudo docker run -i -t /bin/bash
```
Una vez logeados en el terminal del contenedor, ejecutamos:
```bash
sh ejecucion_desde_docker.sh
```
### Uso de base de datos remota
Si en la ejecución con Docker (en cualquiera de las 2 opciones) se desea usar una base de datos remota, una vez en el terminal del contenedor se debe ejecutar:
```bash
unset USINGDOCKER
unset DOCKERMULTIPLE
```

Y proceder a la definición de la variable de entorno necesaria tal y como se detalla en el apartado ["Ejecución en local"](https://github.com/juanjetomas/ProyectoIV#en-local) de este mismo fichero de documentación.


Para más información sobre este apartado, consultar la [documentación del Hito 4](https://github.com/juanjetomas/ProyectoIV/blob/documentacion/Hito4.md).

## Deslpiegue automático
El objetivo de este apartado es realizar el despliegue automático en una máquina virtual del tipo IaaS remota. Podemos dividir este proceso en creación de la máquina virtual y orquestación, provisionamiento y despliegue.

### Creación de la máquina virtual
Para la creación y orquestación de la máquina virtual se ha usado Vagrant, y el IaaS elegido ha sido Azure. Para este cometido se usa el archivo [Vagrantfile](Vagrantfile) que se muestra a continuación:

```ruby
Vagrant.configure('2') do |config|
  config.vm.box = 'azure'
  config.vm.box_url = 'https://github.com/msopentech/vagrant-azure/raw/master/dummy.box' #Caja base vacía
  config.vm.network "private_network",ip: "192.168.50.4", virtualbox__intnet: "vboxnet0" #Ip privada
  config.vm.hostname = "localhost"
  config.vm.network "forwarded_port", guest: 80, host: 80

  # use local ssh key to connect to remote vagrant box
  config.ssh.private_key_path = '~/.ssh/id_rsa'

  config.vm.provider :azure do |azure, override|

    # use Azure Active Directory Application / Service Principal to connect to Azure
    # see: https://azure.microsoft.com/en-us/documentation/articles/resource-group-create-service-principal-portal/

    # each of the below values will default to use the env vars named as below if not specified explicitly

    azure.vm_image_urn = 'canonical:UbuntuServer:16.04-LTS:16.04.201701130' #Imagen base del sistema
    azure.vm_size = 'Basic_A0' #Tamaño (recursos) de la MV
    azure.location = 'westeurope'
    azure.vm_name = 'MVbaresytapas'
    azure.tcp_endpoints = '80:80'
    azure.vm_password = 'pass'

    azure.tenant_id = ENV['AZURE_TENANT_ID']
    azure.client_id = ENV['AZURE_CLIENT_ID']
    azure.client_secret = ENV['AZURE_CLIENT_SECRET']
    azure.subscription_id = ENV['AZURE_SUBSCRIPTION_ID']
  end

  #Provisionamiento
  config.vm.provision "ansible" do |ansible|
        ansible.sudo = true
        ansible.playbook = "configuracion.yml"
        ansible.verbose = "-vvvv"
        ansible.host_key_checking = false
  end

end
```
Este fichero define la creación de la máquina virtual y todos los parámetros que la conforman como por ejemplo:
* IaaS
* Caja base (la cual está vacía y completamos posteriormente)
* Método de autentificación por SSH
* Imagen base del distema (en este caso: Ubuntu server 16.04)
* Tamaño de la máquina virtual (y por ende, cantidad de recursos disponibles)
* Localización de la máquina
* Credenciales de Azure (para más información sobre su obtención y definición, consultar la [documentación de este proyecto](https://github.com/juanjetomas/ProyectoIV/blob/documentacion/Hito5.md))
* Y por último el método de provisionamiento, que en este caso se hace con Ansible, como se muestra en el siguiente apartado.

**Nota**: Por el reciente cambio de APIs es posible que el puerto HTTP no quede correctamente abierto, si esto ocurre puede consultar la solución en la [documentación](https://github.com/juanjetomas/ProyectoIV/blob/documentacion/Hito5.md)

Se ejecuta con el comando:
```bash
vagrant up --provider=azure
```

### Provisionamiento de la máquina virtual
Este paso consiste en la instalación del software que requiera la aplicación independientemente de su modo de ejecución (definido en la siguiente sección). Dichas especificaciones están definidas en el fichero de Ansible [configuracion.yml](configuracion.yml) que se muestra a continuación:
```
---
- hosts: all
  sudo: yes
  remote_user: vagrant
  tasks:
  - name: Actualizar el sistema
    command: sudo apt-get update
  - name: Dependencias basicas
    action: apt pkg={{ item }} state=present
    with_items:
      - python3-setuptools
      - python3-dev
      - libpq-dev
      - build-essential
      - git
      - gunicorn
  - name: Instalar pip
    command: sudo easy_install3 pip
```
En esta fase se realizan tareas como:
* La actualización de los repositorios
* Instalación de:
  * Herramientas de Python (necesarias para la ejecución del proyecto)
  * Git (que para clonar el repositorio)
  * Gunicorn (para lanzar la aplicación)

**Nota**: Aunque no forma parte del archivo de configuración de Ansible en sí, se recomienda la definición del archivo [ansible.cfg](ansible.cfg) para evitar errores relacionados con cadenas demasiado largas que se usan durante el provisionamiento.

### Despliegue
En esta fase final se proveen las herramientas para una fácil descarga de la aplicación y su posterior lanzamiento. Además permite controlar su ciclo de vida. Todo esto se realiza con Fabric y su configuración está especificada en el fichero [fabfile.py](fabfile.py), que se muestra a continuación:
```python
#coding: utf-8
from fabric.api import run, local, hosts, cd, env, sudo, settings
from fabric.contrib import django
from fabric.operations import put
from fabric.context_managers import hide
from io import StringIO

env.use_ssh_config = True

#Clona el repositorio e instala las dependencias
def instala(clavebd=""):
    run('sudo rm -rf ProyectoIV/')
    run('sudo git clone https://github.com/juanjetomas/ProyectoIV.git')
    run('cd ProyectoIV && sudo pip install -r requirements.txt')
    if clavebd =="": #Si no se pasa parámetro la base de datos es local
        #Intalación de los paquetes de postgres
        run('sudo apt-get install -y postgresql postgresql-contrib')
        #Se crea la base de datos y el usuario necesario
        sudo('psql -c "CREATE USER baresytapasuser WITH SUPERUSER PASSWORD \'baresyTapasPassword\';"', user='postgres')
        sudo('psql -c "CREATE DATABASE baresytapas WITH OWNER baresytapasuser;"', user='postgres')
        run('sudo service postgresql start')
        #Se realiza la migración y se popula la base de datos
        run('cd ProyectoIV && python3.5 manage.py migrate && python3.5 populate_rango.py')
        archivo = StringIO()
        #Se crea un archivo para indicar la variable de entorno que indica la bd local
        archivo.write(u'''PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games"\nUSINGDOCKER="TRUE"''')
        put(archivo, "/home/vagrant/environment")
        run('sudo rm -rf /etc/environment')
        #Se copia dicho archivo
        run('sudo cp /home/vagrant/environment /etc/environment')

    else:
        clavedbunicode = clavebd.decode('utf-8')
        archivo = StringIO()
        #Se crea un archivo que indica la contraseña de la bd remota
        archivo.write(u'''PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games"\nPASSDBVARIABLE="''')
        archivo.write(clavedbunicode)
        archivo.write(u'''"''')
        put(archivo, "/home/vagrant/environment")
        run('sudo rm -rf /etc/environment')
        run('sudo cp /home/vagrant/environment /etc/environment')

#Ejecuta el set de tests definidos en tests.py
def test():
    run('cd /home/vagrant/ProyectoIV && python3.5 manage.py test')


#Inicia la aplicación y usa cron junto a un pequeño script que comprueba que se ejecute constantemente
def arranca():
    with settings(
        hide('warnings', 'running', 'stdout', 'stderr'),
        warn_only=True
    ):
        #Si psql está instlado, arranca la bd local
        run('which psql')
        run('if [ "$?" -eq "0" ]; then\n sudo service postgresql restart \n fi')

    #Crea la tarea que se ejecuta cada minuto para comprobar el estado de la aplicación
    run('sudo chmod +x /home/vagrant/ProyectoIV/comprueba_ejecucion.sh')
    run('crontab -l | { cat; echo "* * * * * /home/vagrant/ProyectoIV/comprueba_ejecucion.sh"; } | crontab -')

    #Lanza la aplicación
    run('cd /home/vagrant/ProyectoIV &&  nohup sudo -E gunicorn tango_with_django_project.wsgi -b 0.0.0.0:80 &', pty=False)

#Para la aplicación y detiene el cron que comprueba su ejecución
def para():
    #Detiene la aplicación
    run('sudo killall gunicorn || true')
    with settings(
        hide('warnings', 'running', 'stdout', 'stderr'),
        warn_only=True
    ):
        #Elimina el cron que la ejecutaba
        run('crontab -r')
```
La funcionalidad de las funciones definidas es:
* **instala**: Realiza la instalación de la aplicación:
  * Clona el repositorio
  * Instala las Dependencias
  * Si no se define clave para la base de datos remota:
    * Instala ``postgresql``
    * Crea el usuario de la base de datos
    * Crea la base de datos
    * Migra la base de datos
    * Popula la base de datos
    * Define una variable de entorno que indica el uso de base de datos local
  * Si se define una clave para la base de datos remota:
    * Crea una variable de entorno con dicha clave
* **test**: Ejecuta los test definidos en [tests.py](rango/tests.py)
* **arranca**: Lanza la aplicación.
  * Si hay una base de datos instalada, la arranca.
  * Crea una tarea que comprueba cada minuto que se ejecuta la aplicación (la explicación de esta solución se encuentra en la [documentación](https://github.com/juanjetomas/ProyectoIV/blob/documentacion/Hito5.md))
  * Ejecuta la aplicación
* **para**: Detiene la aplicación
  * Se detiene la aplicación
  * Se elimina la comprobación

**Nota**: las decisiones tomadas respecto a la instalación de paquetes en este paso y al método de supervisión de la aplicación están discutidas en la [documentación](https://github.com/juanjetomas/ProyectoIV/blob/documentacion/Hito5.md).

Con el siguiente _fabfile.py_ la ejecución se haría siguiendo este esquema:
```bash
fab -H usuariomv@url.de.la.mv funcion
```
En nuestro caso, si queremos realizar la instalación usando una base de datos remota:
```bash
fab -H vagrant@bitter-breeze-8.westeurope.cloudapp.azure.com instala:<contraseña>
```
Consulte la sección ["Ejecución en local"](https://github.com/juanjetomas/ProyectoIV#en-local) de este mismo documento para la especificación de la _contraseña_.

O si por el contrario queremos usar una base de datos local, haríamos:
```bash
fab -H vagrant@bitter-breeze-8.westeurope.cloudapp.azure.com instala
```

Una vez realizados todos los pasos mencionados, podemos encontrar nuestra aplicación desplegada en Azure [aquí]().
