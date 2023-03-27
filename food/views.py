from django.shortcuts import render
from django.http import HttpResponse
from .models import Pie, Cake, Donut
from django.views.decorators.csrf import csrf_exempt


def index(request):
    ctx = {'name': 'OBLIVIOUS BAKERY'}
    return render(request, "food/index.html", ctx)


def pie(request):
    pies = Pie.objects.all()
    ctx = {'pies': pies}
    print(pies)
    return render(request, "food/pies.html", ctx)


def cakes(request):
    cakes = Cake.objects.all()
    ctx = {'cakes': cakes}
    print(cakes)
    return render(request, "food/cakes.html", ctx)


def donut(request):
    donuts = Donut.objects.all()
    ctx = {'donuts': donuts}
    print(donuts)
    return render(request, "food/donuts.html", ctx)


@csrf_exempt
def order(request):
    if request.is_ajax():
        test = request.POST.get['test']
        print(test)
    ctx = {'active_link': 'order'}
    return render(request, "food/order-list.html", ctx)

