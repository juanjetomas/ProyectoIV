from django.contrib import admin
from rango.models import Bares, Tapas


class BaresAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('nombre',)}

# Update the registeration to include this customised interface
admin.site.register(Bares, BaresAdmin)
admin.site.register(Tapas)

# Register your models here.
