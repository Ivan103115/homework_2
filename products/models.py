from django.db import models

# Create your models here.


class Product(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    rate = models.FloatField()
    price = models.FloatField()
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)


class Review(models.Model):
    title = models.TextField()
    characteristics = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
