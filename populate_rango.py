import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from rango.models import Bares, Tapas


def populate():
	bar_damian = add_bar(name="Casa Damian", dire="Carretera de Jaen", visit = 74 )

	add_tapa(barp=bar_damian,
		nom="Jamon Asado",
		url="http://docs.python.org/2/tutorial/")

	add_tapa(barp=bar_damian,
		nom="Jamon Serrano",
		url="http://www.forocoches.com")

	bar_posada = add_bar("Posada", "C/Periodista Daniel Saucedo Aranda" )

	add_tapa(barp=bar_posada,
		nom="Rosca",
		url="http://www.google.es")

	add_tapa(barp=bar_posada,
		nom="Hamburguesa",
		url="http://www.google.mx")

	bar_rialca = add_bar("Rialca", "Calle Tortola 7" )

	add_tapa(barp=bar_rialca,
		nom="Cafe Chismiqui",
		url="http://www.minijuegos.com")

	add_tapa(barp=bar_rialca,
		nom="Cafe Dopaico",
		url="http://imdb.com")



    # Print out what we have added to the user.
	for c in Bares.objects.all():
		for p in Tapas.objects.filter(bar=c):
			print "- {0} - {1}".format(str(c), str(p))

def add_bar(name, dire, visit=0):
	c = Bares.objects.get_or_create(nombre=name)[0]
	c.direccion = dire
	c.visitas = visit
	c.save()
	return c

def add_tapa(barp, nom, url, vot=0):
	p = Tapas.objects.get_or_create(bar=barp, nombre=nom)[0]
	p.votos = vot
	p.url = url
	p.save()
	return p


# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()
