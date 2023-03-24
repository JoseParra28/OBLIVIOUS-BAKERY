from django.contrib import admin
from .models import Pie, Cake


class Pie_admin(admin.ModelAdmin):
    list_display = ('name', 'price_m', 'price_l')


admin.site.register(Pie, Pie_admin)
admin.site.register(Cake, Pie_admin)
