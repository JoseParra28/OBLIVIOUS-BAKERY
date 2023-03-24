from django.contrib import admin
from .models import Pie, Cake, Donut


class Pie_admin(admin.ModelAdmin):
    list_display = ('name', 'price_m', 'price_l')


admin.site.register(Pie, Pie_admin)


class Cake_admin(admin.ModelAdmin):
    list_display = ('name', 'price_m', 'price_l')


admin.site.register(Cake, Cake_admin)


class Donut_admin(admin.ModelAdmin):
    list_display = ('name', 'price_m', 'price_l')


admin.site.register(Donut, Donut_admin)
