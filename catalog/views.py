from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy, reverse
from catalog.models import Product, Blog


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    return render(request, 'catalog/contacts.html')


def pictures(request):
    context = {
        'object_list': Product.objects.all()
    }
    return render(request, 'catalog/pictures.html', context)


class ProductListView(ListView):
    model = Product


class BlogListView(ListView):
    model = Blog

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(sign_of_publication=Blog.STATUS_ACTIVE)

        return queryset


class BlogCreateView(CreateView):
    model = Blog
    fields = '__all__'
    success_url = reverse_lazy('catalog:blog')


class BlogUpdateView(UpdateView):
    model = Blog
    fields = '__all__'
    success_url = reverse_lazy('catalog:blog')


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog')


class BlogDetailView(DetailView):
    model = Blog

    def views_counter(self, request, pk):
        blog_item = get_object_or_404(Blog, pk=pk)
        blog_item.views_number += 1
        blog_item.save()
        return super().get(self, request, pk)


def change_status(request, pk):
    blog_item = get_object_or_404(Blog, pk=pk)
    if blog_item.sign_of_publication == Blog.STATUS_ACTIVE:
        blog_item.sign_of_publication = Blog.STATUS_INACTIVE
    else:
        blog_item.sign_of_publication = Blog.STATUS_ACTIVE
    blog_item.save()

    return redirect(reverse('catalog:blog'))
