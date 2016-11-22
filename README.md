# Proyecto Infraestructura Virtual (IV) curso 16/17
[![Build Status](https://travis-ci.org/juanjetomas/ProyectoIV.svg?branch=master)](https://travis-ci.org/juanjetomas/ProyectoIV)

[![Heroku](https://iwantmyname.com/images/logo-developer-heroku.png)](https://baresytapasjj.herokuapp.com/rango/)


[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

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
Contando con (por ejemplo) un fork del repositorio, se puede realizar el despliegue automático desde Github. Se puede consultar el proceso en el [siguiente enlace](https://github.com/juanjetomas/ProyectoIV/blob/documentacion/Hito3.md#despliegue-automático).


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
