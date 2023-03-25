from django.shortcuts import render
from django.http import HttpResponse
from .models import Pie, Cake, Donut


def index(request):
    ctx = {'name': 'OBLIVIOUS BAKERY'}
    return render(request, "food/index.html", ctx)


def pie(request):
    pies = Pie.objects.all()
    ctx = {'pies': pies}
    print(pies)
    return render(request, "food/pies.html", ctx)


def cakes(request):
    return render(request, "food/cakes.html")




