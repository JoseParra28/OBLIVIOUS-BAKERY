from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    ctx = {'name': 'OBLIVIOUS BAKERY'}
    return render(request, "food/index.html", ctx)


def pie(request):
    ctx = {'name': 'OBLIVIOUS BAKERY'}
    return render(request, "food/pie.html")





