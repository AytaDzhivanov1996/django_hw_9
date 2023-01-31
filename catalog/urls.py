from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, contacts, ProductListView, pictures, BlogListView, BlogCreateView, BlogUpdateView, \
    BlogDeleteView, BlogDetailView, change_status, ProductCreateView, ProductDetailView, ProductUpdateView, \
    ProductDeleteView, ProductUpdateWithVersionView

app_name = CatalogConfig.name

urlpatterns = [
    path('', home),
    path('contacts/', contacts),
    path('products/pictures/', pictures),
    path('products/', ProductListView.as_view(), name='product'),
    path('products/create/', ProductCreateView.as_view(), name='create_product'),
    path('products/update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('products/delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('products/detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/update/<int:pk>/version/', ProductUpdateWithVersionView.as_view(), name='update_product_version'),
    path('products/blog/', BlogListView.as_view(), name='blog'),
    path('products/blog/create/', BlogCreateView.as_view(), name='create'),
    path('products/blog/update/<int:pk>/', BlogUpdateView.as_view(), name='update'),
    path('products/blog/delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
    path('products/blog/detail/<int:pk>/', BlogDetailView.as_view(), name='detail'),
    path('products/blog/status/<int:pk>/', change_status, name='status')
]
