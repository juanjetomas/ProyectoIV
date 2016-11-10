from django.conf.urls import patterns, url
from rango import views
from django.conf import settings

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
		url(r'^about/', views.about, name='about'),
		url(r'^bar/(?P<bar_name_slug>[\w\-]+)/$', views.bar, name='bar'),  # New!)
		url(r'^add_bar/$', views.add_bar, name='add_bar'),
		#url(r'^add_tapa/$', views.add_tapa, name='add_tapa'),) # NEW MAPPING!
		url(r'^bar/(?P<bar_name_slug>[\w\-]+)/add_tapa/$', views.add_tapa, name='add_tapa'),
		url(r'^reclama_datos/$', views.reclama_datos, name='reclama_datos'), #Para dibujar la grafica
        url(r'^lista_bares/$', views.lista_bares, name='lista_bares')
        ,) #Para dibujar la graficaz



if settings.DEBUG:
	urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
