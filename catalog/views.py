from django.shortcuts import render
from catalog.models import Product


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    return render(request, 'catalog/contacts.html')


def products(request):
    context = {
        'product_list': Product.objects.all()
    }
    return render(request, 'catalog/products.html', context)


def pictures(request):
    context = {
        'pictures_list': Product.objects.all()
    }
    return render(request, 'catalog/pictures.html', context)
