# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm, ValidationError
from django.forms.util import ErrorList


from customers.models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer