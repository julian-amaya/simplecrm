# -*- coding: utf-8 -*-

from django.template.context import RequestContext
from django.shortcuts import render_to_response, get_object_or_404


from customers.models import Company, Customer
from customers.forms import CustomerForm

def index(request):
    data = {}
    #TALLER - organizar las empresas por nombre?
    data['companies'] = Company.objects.all()
    return render_to_response('index.html', data, context_instance=RequestContext(request))

# taller crear vista para una empresa
def company(request, id_company):
    data = {}
    # paso 1 - buscar la empresa!!
    # paso 2 - traer los clientes   
    #paso 3 - agregar formulario para agregar un nuevo cliente
    #paso 4 - grabar si ya vienen datos!!
    return render_to_response('company.html', data, context_instance=RequestContext(request))

