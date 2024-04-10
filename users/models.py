from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLES = (
        ('client', 'Клиент'),
        ('trainer', 'Тренер'),
        ('admin', 'Админ'),
    )
    role = models.CharField(max_length=10, choices = ROLES)


    class Meta:
        verbose_name= 'Пользователь'
        verbose_name_plural = "Пользователи"

   
