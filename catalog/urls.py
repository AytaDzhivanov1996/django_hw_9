from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, contacts, products, pictures

app_name = CatalogConfig.name

urlpatterns = [
    path('', home),
    path('contacts/', contacts),
    path('products/', products),
    path('products/pictures/', pictures)
]
