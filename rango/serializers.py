
from rest_framework import serializers
from rango.models import Bares

class BarSerializer(serializers.ModelSerializer):
	class Meta:
		model = Bares
		fields = ("nombre", "direccion", "visitas",)
