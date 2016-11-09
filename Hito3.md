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
