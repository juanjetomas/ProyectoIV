#!/bin/bash
if [[ ! `ps aux |grep gunicorn | grep tango` ]]; then
        cd /home/vagrant/ProyectoIV &&  nohup sudo -E gunicorn tango_with_django_project.wsgi -b 0.0.0.0:80 &
fi
