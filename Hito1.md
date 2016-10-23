# Práctica 1:Aplicación sobre la que se creará la infraestructura virtual
La infraestructura virtual se pretende crear sobre una aplicación web, desarrollada usando Python mediante el framework Django. La aplicación mostraría una lista de bares con sus repectivas tapas y permitiría tanto añadir nuevos, como votar las tapas favoritas, permitiendo hacer rankings. Los usuarios podrían registrarse.

La base de datos principal sería PostgreSQL. Se usaría un servicio de log como LogStash, Elasticsearch indexaría dichos datos y, opcionalmente, Kibana los mostraría en una interface web.

El despliegue se realizará en principio en Amazon Web Services, aunque puede cambiar si durante el desarrollo de la asignatura se encuentra uno con más ventajas.
