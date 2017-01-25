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
