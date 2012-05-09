from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #URL de listado de clientes
    url(r'^$', 'customers.views.index', name='home'),

    # TALLER agregar la url para la vista de cada cliente
	url(r'^c/(?P<id_company>(\d)+)/$', 'customers.views.company', name='company'),
    
    url(r'^admin/', include(admin.site.urls)),
)
