# Hito 2: Integración continua en el repositorio

## Requisitos
En primer lugar, he creado el archivo _requirements.txt_ que contiene las dependencias de mi aplicación, que por ahora son pocas:

``` python
Django==1.7
django-registration==2.1.2
psycopg2==2.6.2
```

## Tests
Para realizar la integración continua, han de realizarse una serie de tests. En mi caso, he optado por utilizar la herramienta integrada que usa Django ([testing in Django](https://docs.djangoproject.com/es/1.10/topics/testing/)).

Estos se incluyen en el archivo _tests.py_ que se muestra a continuación (los test se iran ampliando según las necesidades de la aplicación):

```python
from django.test import TestCase

from rango.models import Bares
from rango.models import Tapas
from rango.forms import BaresForm
from rango.forms import TapasForm
from .views import *
from django.test.client import Client
import unittest
from django.core.urlresolvers import reverse


# Create your tests here.

class BaresTestCase(TestCase):
    def test_check_form_bar(self):
        formdata = {
            'nombre':'nombretest',
            'visitas': 5,
            'direccion': 'nombrestest',
        }
        form = BaresForm(data=formdata)
        self.assertTrue(form.is_valid())
        print "\nEl formulario utilizado es válido"

    def test_save_bar(self):
        formdata = {
            'nombre':'nombretest',
            'visitas': '5',
            'direccion': 'nombrestest',
        }
        form = BaresForm(data=formdata)
        form.save(commit=True);
        global lista
        try:
            lista = Bares.objects.get(slug="nombretest")
        except Bares.DoesNotExist:
            lista=[]
        self.assertTrue(lista)
        print  "\n" + lista.nombre
        print "\nEl bar se ha guardado correctamente"

    def test_show_bares(self):
        formdata = {
            'nombre':'nombretest2',
            'visitas': '6',
            'direccion': 'nombrestest2',
        }
        form = BaresForm(data=formdata)
        form.save(commit=True);

        formdata = {
            'nombre':'nombretest3',
            'visitas': '9',
            'direccion': 'nombrestest3',
        }
        form = BaresForm(data=formdata)
        form.save(commit=True);
    	bares_list = Bares.objects.order_by('-visitas')[:10]
        nbar = 1
    	for bar in bares_list:
            print "\nBar " +str(nbar) + " " + bar.nombre
            nbar = nbar+1
        print "\nLista de bares accedida correctamente"

class TestStringMethods(unittest.TestCase):
	def test_index(self):

		c = Client()

		respose = c.get(reverse('index'))
		self.assertEqual(respose.status_code,200)
        print "\nAcceso correcto como cliente"
```


Una vez hecho esto, mediante el comando
```bash
python manage.py test
```
Se ejecutan los test tal y como se aprecia en la prueba local (aunque con la base de datos ya en AWS):
![img6](capturas/captura6.png)

## Configuración de la base de datos
Como se ha comentado anteriormente, se ha configurado una instancia de PostgreSQL en Amazon Web Services. Estos han sido los pasos de forma resumida:

Se accede a la [consola de AWS](https://eu-central-1.console.aws.amazon.com/rds/home?region=eu-central-1#launch-dbinstance:ct=dbinstances) y se selecciona PostgreSQL:

![img10](capturas/captura10.png)

![img11](capturas/captura11.png)

Configuramos la base de datos con el nombre, usuario y contraseña:

![img12](capturas/captura12.png)

Y tras rellenar los últimos datos, lanzamos la instancia:

![img13](capturas/captura13.png)

Tras esto, descargamos e instalamos pgAdmin para administrar nuestra base de datos:
```bash
sudo apt-get install wget ca-certificates
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install postgresql-9.5 pgadmin3
```

Una vez dentro de pgadmin hacemos click en _File, add server_ y rellenamos con los datos de nuestro servidor de AWS:
![img14](capturas/captura14.png)

Seleccionamos la base de datos dentro del servidor y procedemos a restaurar la copia que teníamos en local:

![img15](capturas/captura15.png)

Y añadimos el archivo _.backup_

![img16](capturas/captura16.png)

A continuación, permitimos al usuario de la base de datos que cree tablas para que se puedan ejecutar correctamente los test (si no, no podrá crear la réplica de la DB para realizar las pruebas)

![img17](capturas/captura17.png)

Finalmente, en la consola de AWS debemos permitir que se pueda acceder a la base de datos desde diferentes direcciones IP, ya que de lo contrario solo se podrán hacer peticiones desde la IP con la que se generó la misma. Esto se hace en el security group:

![img18](capturas/captura18.png)

En la pestaña inbound seleccionamos la o las IPs (en rango, por ejemplo) que pueden acceder al servicio. En este caso se ha dejado acceso desde cualquiera, aunque no es lo más recomendable:

![img19](capturas/captura19.png)44


## Travis
Para realizar la integración contínua con Travis, se crea el archivo _.travis.yml_ que especifica las características del entorno en el que se ejecutarán los test, como el lenguaje usado, las ramas a testear, la instalación de requisitos y la ejecución de las pruebas:

```yml
build_environment: Ubuntu 16.04
# Únicas ramas que ejecutan test
branches:
  only:
  - master

language: python

python:
  - 2.7

install:
  - pip install -r requirements.txt

script:
  - python manage.py test
```

Activamos el acceso al repositorio del proyecto:

![img7](capturas/captura7.png)

Y establecemos las variables de entorno (en este caso se almacena la contraseña de la base de datos)

![img8](capturas/captura8.png)

Se ejecutan los test desde Travis:

![img9](capturas/captura9.png)

Y obtenemos:

[![Build Status](https://travis-ci.org/juanjetomas/ProyectoIV.svg?branch=master)](https://travis-ci.org/juanjetomas/ProyectoIV)
