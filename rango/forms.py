from django import forms
from rango.models import Bares, Tapas

class BaresForm(forms.ModelForm):
    nombre = forms.CharField(max_length=128, help_text="Introduzca el nombre del bar.")
    visitas = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    direccion = forms.CharField(max_length=128, help_text="Introduzca la direccion.")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Bares
        fields = ('nombre','direccion',)


class TapasForm(forms.ModelForm):
    nombre = forms.CharField(max_length=128, help_text="Introduzca el nombre de la tapa.")
    #url = forms.URLField(max_length=200, help_text="Introduzca la url de la tapa.")
    #votos = forms.IntegerField(widget=forms.HiddenInput(), required=False)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Tapas

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form,
        exclude = ('bar','url', 'votos')
        #or specify the fields to include (i.e. not include the category field)
        #fields = ('title', 'url', 'views')
