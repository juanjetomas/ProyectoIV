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
