# -*- coding: utf-8 -*-
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

'''
class TapasTestCase(TestCase):
    def test_add_tapa(self):
        formdata = {
            'nombre':'nombretest4',
            'visitas': '7',
            'direccion': 'nombrestest4',
        }
        form = BaresForm(data=formdata)
        form.save(commit=True);
        global barg
        try:
            barg = Bares.objects.get(slug="nombretest4")
        except Bares.DoesNotExist:
            pass
        t = Tapa(nombre = "tapatest", votos = 4, bar = barg)
        t.save();
        print "Tapa creada con exito"
'''
