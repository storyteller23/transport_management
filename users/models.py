from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    ROLES = (
        ('B', 'Бухгалтер'),
        ('D', 'Водитель'),
    )
    GENDERS = (
        ('M', 'Мужчина'),
        ('F', 'Женщина'),
    )

    fullname = models.CharField(max_length=255, default='', verbose_name='ФИО')
    gender = models.CharField(max_length=1, choices=GENDERS, default='', verbose_name='Пол')
    birth_date = models.DateField(default='1970-01-01', verbose_name='Дата рождения')
    role = models.CharField(max_length=1, choices=ROLES, default='D', verbose_name='Должность')