## Práctica 0
A continuación se muestran los pasos seguidos en la realización de la práctica.
# Creación de par de claves y subida de clave a GitHub
Las claves se generan con el siguiente comando:

```bash
ssh-keygen -t rsa -b 4096 -C "juanjetomas@hotmail.com"
```

Tras esto, se indica en qué lugar se guardan las claves y si se desea usar un passphrase.

A continuación, se comprueba que el agente ssh está funcionado con:

```bash
eval "$(ssh-agent -s)"
```

Y se añade la clave SSH al agente con:

```bash
ssh-add ~/.ssh/id_rsa
```

En el menú de la web, vamos a settings, SSH and GPC keys, new SSH key. Se pega el contenido de id_rsa.pub en el campo Key:

![img1](https://github.com/juanjetomas/ProyectoIV/blob/hito0/capturas/captura1.png)

# Repositorio principal, milestones e issues

Tras pulsar en new repository, rellenamos los datos del mismo:

![img2](https://github.com/juanjetomas/ProyectoIV/blob/hito0/capturas/captura2.png)

Creamos una carpeta en local donde se albergará nuestro proyecto, y la inicializamos con:

```bash
git init
```

Tras esto realizamos la configuración del correo y nombre:
```bash
git config --global user.name "Juan Jesús Tomás Rojas"
git config --global user.email "juanjetomas@hotmail.com"
```

Añadimos el repositorio:
```bash
git remote add origin git@github.com:juanjetomas/ProyectoIV.git
```

Enviamos el proyecto al repositorio remoto
```bash
git push -u origin master
```

Tras esto, en la web, se crea el primer milestone:

![img3](https://github.com/juanjetomas/ProyectoIV/blob/hito0/capturas/captura3.png)

Una vez dentro del milestone, creamos los diferentes issues para cada una de las tareas a realizar (license, readme y gitignore):

![img4](https://github.com/juanjetomas/ProyectoIV/blob/hito0/capturas/captura4.png)

# Cerrando los issues
Se añaden los archivos y en el mensaje se indica que cierran el issue con su número.
```bash
git add .gitignore
git commit -m "close #1"
git push -u origin master
git add README.md
git commit -m "close #2"
git push
git add LICENSE
git commit -m "close #3"
git push
```

Tras esto, los issues quedan cerrados y el milestone al 100%:

![img5](https://github.com/juanjetomas/ProyectoIV/blob/hito0/capturas/Captura5.png)

# Clonando el repositorio de la asignatura
Hacemos click en el botón fork del repositorio JJ/IV16-17
Nos situamos en la carpeta que nos interesa y realizamos:
```bash
git clone git@github.com:juanjetomas/IV16-17.git
```

# Creando una rama de nuestro repositorio
Tras colocarnos en la carpeta de nuestro proyecto, comprobamos que estamos en master:
```bash
git checkout master
```
Creamos la rama hito0:
```bash
git checkout -b hito0
```
Añadimos los archivos y realizamos el push a la rama:
```bash
git add capturas/*
git add hito0.md
git commit -m "Compiezo práctica 0"
git push origin hito0
```

# Realizando el pull request
Se añaden los archivos de la manera habitual y se selecciona "New pull request"

