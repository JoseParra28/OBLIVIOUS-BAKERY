from django.db import models


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




