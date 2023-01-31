from django.core.management import BaseCommand
import datetime
from catalog.models import Blog


class Command(BaseCommand):

    def handle(self, *args, **options):
        blogs = [
            {'head': 'rambutan', 'slug': 'rambutan', 'content': 'hairy red', 'image': 'rambutan.jpg',
             'creation_date': datetime.date.today()},
            {'head': 'peaches', 'slug': 'peaches', 'content': 'hairy orange', 'image': 'peaches.jpg',
             'creation_date': datetime.date.today()}
        ]

        blogs_list = []

        for item in blogs:
            blogs_list.append(Blog(**item))

        Blog.objects.all().delete()
        Blog.objects.bulk_create(blogs_list)
