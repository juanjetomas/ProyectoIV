from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Bares
from rango.models import Tapas
from rango.forms import BaresForm
from rango.forms import TapasForm
from django.http import JsonResponse

def index(request):

	# Construct a dictionary to pass to the template engine as its context.
	# Note the key boldmessage is the same as {{ boldmessage }} in the template!
	bares_list = Bares.objects.order_by('-visitas')[:10]
	context_dict = {'bares': bares_list }

	# Return a rendered response to send to the client.
	# We make use of the shortcut function to make our lives easier.
	# Note that the first parameter is the template we wish to use.

	return render(request, 'rango/index.html', context_dict)

def bar(request, bar_name_slug):

	# Create a context dictionary which we can pass to the template rendering engine.
	context_dict = {}

	try:
		# Can we find a category name slug with the given name?
		# If we can't, the .get() method raises a DoesNotExist exception.
		# So the .get() method returns one model instance or raises an exception.
		bar = Bares.objects.get(slug=bar_name_slug)
		context_dict['bar_name'] = bar.nombre
		context_dict['bar_name_url'] = bar_name_slug 

		# Retrieve all of the associated pages.
		# Note that filter returns >= 1 model instance.
		tapas = Tapas.objects.filter(bar=bar)

		# Adds our results list to the template context under name pages.
		context_dict['tapas'] = tapas
		# We also add the category object from the database to the context dictionary.
		# We'll use this in the template to verify that the category exists.
		context_dict['bar'] = bar
		bar.visitas+=1
		bar.save()
	except Bares.DoesNotExist:
		# We get here if we didn't find the specified category.
		# Don't do anything - the template displays the "no category" message for us.
		pass

	# Go render the response and return it to the client.
	return render(request, 'rango/bar.html', context_dict)

def add_bar(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = BaresForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = BaresForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'rango/add_bar.html', {'form': form})

def add_tapa(request, bar_name_slug):

    try:
        bare = Bares.objects.get(slug=bar_name_slug)
    except Bares.DoesNotExist:
                bare = None

    if request.method == 'POST':
        form = TapasForm(request.POST)
        if form.is_valid():
            if bare:
                tapa = form.save(commit=False)
                tapa.bar = bare
                tapa.votos = 0
                tapa.save()
                # probably better to use a redirect here.
                return bar(request, bar_name_slug)
        else:
            print form.errors
    else:
        form = TapasForm()

    context_dict = {'form':form, 'bar_name_url':bar_name_slug, 'bar': bar}	

    return render(request, 'rango/add_tapa.html', context_dict)

#Solicita los datos de los bares para dibujar la grafica
def reclama_datos(request):
	datos={}
	bares_list = Bares.objects.order_by('-visitas')[:10]
	for bar in bares_list:
		datos[bar.nombre] = bar.visitas
	return JsonResponse(datos, safe=False)

def about(request):
	return render(request, 'rango/about.html')

# Create your views here.
