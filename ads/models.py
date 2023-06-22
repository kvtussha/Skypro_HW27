from django.db import models

class Ads(models.Model):
    name = models.CharField(max_length=40, verbose_name='название')
    author = models.CharField(max_length=40, verbose_name='автор')
    price = models.PositiveIntegerField(verbose_name='цена')
    description = models.TextField(max_length=5000, verbose_name='описание')
    address = models.CharField(max_length=200, verbose_name='адрес')
    is_published = models.BooleanField(verbose_name='опубликовано')

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=40, verbose_name='название')

    def __str__(self):
        return self.name