from django.db import models


class Person(models.Model):
    GENDER = (
        ('M', 'M'),
        ('Ж', "Ж"),
        ('Не определился(ась)', 'Не определился(ась)')
    )
    name = models.CharField(max_length=100, verbose_name='Введите имя')
    age = models.PositiveIntegerField(verbose_name='Введите ваш возраст')
    hobby = models.TextField(verbose_name='Укажите ваше хобби')
    gender = models.CharField(max_length=100, choices=GENDER)
    phone_number = models.CharField(max_length=14, default='+996', verbose_name='Ваш номер')

    def __str__(self):
        return self.name