from django.db import models
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.models import User


class Pie(models.Model):
    name = models.CharField(max_length=120)
    price_m = models.CharField(max_length=5)
    price_l = models.CharField(max_length=5)
    p_image = models.URLField()


class Cake(models.Model):
    name = models.CharField(max_length=120)
    price_m = models.CharField(max_length=5)
    price_l = models.CharField(max_length=5)
    p_image = models.URLField()


class Donut(models.Model):
    name = models.CharField(max_length=120)
    price_m = models.CharField(max_length=5)
    price_l = models.CharField(max_length=5)
    p_image = models.URLField()    


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.CharField(max_length=50)
    receipt = models.DecimalField(max_digits=4, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    notes = models.TextField(blank=True, null=True)


class Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    price = models.CharField(max_length=5)
    size = models.CharField(max_length=5)


class Review(models.Model):
    review = models.ForeignKey(User, related_name="reviews", on_delete=models.CASCADE)
    reviewer = models.CharField(max_length=20, null=False, blank=False)
    review_area = models.TextField(max_length=20, null=False, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.id)






