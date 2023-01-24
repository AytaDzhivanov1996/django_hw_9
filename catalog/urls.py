from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, contacts, ProductListView, pictures, BlogListView, BlogCreateView, BlogUpdateView, \
    BlogDeleteView, BlogDetailView, change_status

app_name = CatalogConfig.name

urlpatterns = [
    path('', home),
    path('contacts/', contacts),
    path('products/pictures/', pictures),
    path('products/', ProductListView.as_view()),
    path('products/blog/', BlogListView.as_view(), name='blog'),
    path('products/blog/create/', BlogCreateView.as_view(), name='create'),
    path('products/blog/update/<int:pk>/', BlogUpdateView.as_view(), name='update'),
    path('products/blog/delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
    path('products/blog/detail/<int:pk>/', BlogDetailView.as_view(), name='detail'),
    path('products/blog/staus/<int:pk>/', change_status, name='status')
]
