# Hito 3:Despliegue de una aplicación en un PaaS
## Errores previos
Tras la finalización del hito 2 y al intentar ejecutar la aplicación de nuevo, se recibe un error que no ocurría antes:
```bash
django.db.utils.ProgrammingError: permission denied for relation django_migrations
```
Esto es debido a que el usuario creado para las consultas no tiene derechos de propiedad en la base de datos, y se soluciona desde la consola de psql ejecutando:
```bash
GRANT ALL ON ALL TABLES IN SCHEMA public to baresytapasuser;
GRANT ALL ON ALL SEQUENCES IN SCHEMA public to baresytapasuser;
GRANT ALL ON ALL FUNCTIONS IN SCHEMA public to baresytapasuser;
```
## Integración continua
Aunque la integración continua en Travis CI formó parte del hito anterior, en éste se sigue usando como paso previo al despliegue, realizándose los test.
Se puede consultar en este badge: [![Build Status](https://travis-ci.org/juanjetomas/ProyectoIV.svg?branch=master)](https://travis-ci.org/juanjetomas/ProyectoIV)

## Despliegue en PaaS
El PaaS que he elegido es Heroku. Se integra correctamente con Travis y además permite instanciar una base de datos PostgreSQL sin necesidad de introducir una tarjeta de crédito, por lo que se adapta a las necesidades del proyecto.

He seguido [este tutorial](https://devcenter.heroku.com/articles/deploying-python) de la página de Heroku.

En primer lugar he creado el archivo _runtime.txt_ con el siguiente contenido:
```
python-2.7.12
```
```
python-2.7.12
```
Y añadimos al _requirements.txt_:
```
gunicorn==19.6.0
```
Creamos el archivo _Procfile_ para indicar de qué manera se ejecuta la aplicación, con el siguiente contenido:
```
web: gunicorn tango_with_django_project.wsgi --log-file -
```
Tras loguearnos en Heroku toolbelt, creamos la aplicación:

![img20](capturas/captura20.png)

(Es recomendable añadir _--region eu_ en la creación de la app, queda pendiente la migración de la mostrada.)

Indicamos a Heroku la pass de la base de datos de Amazon a la que accede (más adelante se usará una dentro del propio PaaS):
```bash
heroku config:set PASSDBVARIABLE=****
```

Y realizamos el primer despliegue con:
```bash
git push heroku master
```

![img21](capturas/captura21.png)

Se despliega correcamente y podemos acceder con el enlace:
https://baresytapasjj.herokuapp.com/

#### Uso de la base de datos de Heroku
Como hasta ahora la base de datos utilizada es una alojada en AWS, vamos a añadir una opción para que cuando la aplicación se ejecute en Heroku use su propia base de datos.

Instalamos el paquete _dj_database_url_ mediante pip:
```bash
pip install dj_database_url
```
Y lo añadimos al _requirements.txt_. Este paquete nos permite configurar la base de datos de la aplicación mediante una URL.

A continuación, en _settings.py_ se añade la configuración de la base de datos de Heroku mediante URL. A dicha URL se accede a traves de una variable de entorno que se define automáticamente por el propio Heroku.

```python
HEROKU_DEPLOY = os.getenv('DYNO_RAM')
if HEROKU_DEPLOY:
    db_from_env = dj_database_url.config(conn_max_age=500)
    DATABASES['default'].update(db_from_env)
```

Realizamos un push a Heroku, y a continuación:
```bash
heroku run python manage.py migrate
heroku run python populate_rango.py
```
_El último comando es opcional aunque es útil para comprobar que se puede leeer información de la BD correctamente._

Y ya podemos acceder a la aplicación usando la base de datos de Heroku:
https://baresytapasjj.herokuapp.com/

![img22](capturas/captura22.png)

## Despliegue automático
En la pestaña deploy de nuestra aplicación en Heroku:
* Realizamos la conexión con Github
* Seleccionamos nuestro repositorio
* Activamos la opción "Wait for CI to pass before deploy" para que no se despliegue hasta que no se hayan pasado los test
* Y activamos "enable automatic deploy" para que de despligue la aplicación automáticamente con cada push

Tras esto, para comprobar que todo está correcto, modificamos el apartado "Acerca de" y realizamos un push a mi repositorio.

![img23](capturas/captura23.png)

![img24](capturas/captura24.png)

![img25](capturas/captura25.png)

Tras pasar los test en Travis, la aplicación se despliega automáticamente y los cambios se ven reflejados.
