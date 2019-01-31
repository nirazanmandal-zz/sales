from django.shortcuts import render, redirect
from .models import Product
from .form import ProductForm


# Create your views here.
def create(request):
    context = {}
    form = ProductForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('#')
