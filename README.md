# Proyecto Infraestructura Virtual (IV) curso 16/17
[![Build Status](https://travis-ci.org/juanjetomas/ProyectoIV.svg?branch=master)](https://travis-ci.org/juanjetomas/ProyectoIV)

[![Heroku](https://iwantmyname.com/images/logo-developer-heroku.png)](https://baresytapasjj.herokuapp.com/rango/)


[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

[![Dockerhub](https://raw.githubusercontent.com/beatcracker/PSDockerHub/master/Media/PSDockerHub.png)](https://hub.docker.com/r/juanjetomas/proyectoiv/)

[![Azure](https://github.com/juanjetomas/ProyectoIV/blob/documentacion/capturas/azure.png)](https://hub.docker.com/r/juanjetomas/proyectoiv/)

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
* Credenciales de Azure (para más información sobre su obtención y definición, consultar la [documentación de este proyecto](enlacealadocu))
* Y por último el método de provisionamiento, que en este caso se hace con Ansible, como se muestra en el siguiente apartado.

**Nota**: Por el reciente cambio de APIs es posible que el puerto HTTP no quede correctamente abierto, si esto ocurre puede consultar la solución en la [documentación]()
