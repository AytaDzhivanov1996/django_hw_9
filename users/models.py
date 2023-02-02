from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='Почта', unique=True)
    phone = models.CharField(max_length=25, verbose_name='Номер телефона')
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар')
    country = models.CharField(max_length=100, verbose_name='Страна')
    email_confirmed = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

