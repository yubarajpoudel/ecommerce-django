
# Create your models here.
from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="categories")
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="products")
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    brand = models.CharField(max_length=200)
    shipping = models.TextField(blank=True)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rate = models.IntegerField(default=5)
    review = models.TextField()
    created = models.DateTimeField(auto_now_add=True)