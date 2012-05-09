# -*- coding: utf-8 -*-

from django.template.context import RequestContext
from django.shortcuts import render_to_response, get_object_or_404


from customers.models import Company, Customer
from customers.forms import CustomerForm

def index(request):
    data = {}
    #TALLER - organizar los clientes por apellido!
    data['companies'] = Company.objects.all()
    return render_to_response('index.html', data, context_instance=RequestContext(request))

# taller crear vista para una empresa
def company(request, id_company):
    data = {}
    # paso 1 - buscar la empresa!!
    company = get_object_or_404(Company, id=id_company)
    data['company'] = company
    # paso 2 - traer los clientes   
    data['customers'] = company.employees.all()

    #paso 3 - agregar formulario para agregar un nuevo cliente
    if request.method == 'POST':
        cf= CustomerForm(request.POST or None)
        if cf.is_valid():
            c = cf.save()
            cf = CustomerForm()
    else:
        cf= CustomerForm(initial={'company':company})
    data['c_form'] = cf
    return render_to_response('company.html', data, context_instance=RequestContext(request))

def save_employee(request):
    # taller grabar formulario
    f = CustomerForm(request.POST)
    if f.is_valid():
        c = f.save()
        return redirect(c.company.get_absolute_url())
    else:
        data = {}
        # paso 1 - buscar la empresa!!
        company = get_object_or_404(Company, id=id_company)
        data['company'] = company
        # paso 2 - traer los clientes   
        data['customers'] = company.employees.all()

        #paso 3 - agregar formulario para agregar un nuevo cliente
        data['c_form'] = CustomerForm()
        return render_to_response('company.html', data, context_instance=RequestContext(request))

