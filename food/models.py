from django.db import models
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView


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




