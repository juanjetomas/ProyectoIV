from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class Bares(models.Model):
	nombre = models.CharField(max_length=128, unique=True)
	direccion = models.CharField(max_length=128)
	visitas = models.IntegerField(default=0)
	slug = models.SlugField()

	def save(self, *args, **kwargs):
			# Uncomment if you don't want the slug to change every time the name changes
			#if self.id is None:
					#self.slug = slugify(self.name)
			self.slug = slugify(self.nombre)
			super(Bares, self).save(*args, **kwargs)

	def __unicode__(self):  #For Python 2, use __str__ on Python 3
		return self.nombre

class Tapas(models.Model):
	bar = models.ForeignKey(Bares)
	nombre = models.CharField(max_length=128)
	votos = models.IntegerField(default=0)
	url = models.URLField()

	def __unicode__(self):      #For Python 2, use __str__ on Python 3
		return self.nombre
