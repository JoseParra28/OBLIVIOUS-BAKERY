from django.contrib import admin
from .models import Pie, Cake, Donut, Order, Item, Itemm


class Pie_admin(admin.ModelAdmin):
    list_display = ('name', 'price_m', 'price_l')


admin.site.register(Pie, Pie_admin)


class Cake_admin(admin.ModelAdmin):
    list_display = ('name', 'price_m', 'price_l')


admin.site.register(Cake, Cake_admin)


class Donut_admin(admin.ModelAdmin):
    list_display = ('name', 'price_m', 'price_l')


admin.site.register(Donut, Donut_admin)


class Order_admin(admin.ModelAdmin):
    list_display = ('customer', 'number', 'receipt', 'date', 'notes')


admin.site.register(Order, Order_admin)


class Item_admin(admin.ModelAdmin):
    list_display = ('order', 'name', 'price', 'size')


admin.site.register(Item, Item_admin)


class Itemm_admin(admin.ModelAdmin):
    list_display = ('name', 'done')


admin.site.register(Itemm, Itemm_admin)





