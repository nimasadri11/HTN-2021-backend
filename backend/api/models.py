from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255, db_index = True)
    slug = models.SlugField(max_length=255, unique = True)

    class Meta: 
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name = 'product', on_delete = models.CASCADE)
    title = models.CharField(max_length = 255)
    description = models.TextField(blank = True)
    image = models.ImageField(upload_to = 'images/')
    slug = models.SlugField(max_length = 255)
    price = models.DecimalField(max_digits = 4, decimal_places = 2)


    class meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def __str__(self):
        return self.title
