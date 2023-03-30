from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pie, Cake, Donut
from django.contrib.auth.forms import UserCreationForm
from .forms import NewUserForm
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages


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
        request.session['note'] = request.POST.get('note')
        print(request.session['note'])
        orders = request.POST.get('orders')
        print(orders)

    ctx = {'active_link': 'order-list'}
    return render(request, "food/order-list.html", ctx)


def signup(request):
    ctx = {}
    if request.POST:
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            ctx['form'] = form
    else:
        form = NewUserForm()
        ctx['form'] = form
    return render(request, 'food/signup.html', ctx)          


def signInView(request):
    if request.POST:
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(request, username='username', password='pwd')
        if user is not None:
            signInView(request, user)
            return redirect('index')
        else:
            print("invalid")
            messages.info(request, 'Username and/or password are not correct')
        # print("Email:", username)
        # print("Password:", pwd)
    ctx = {'active_link': 'login'}
    return render(request, 'food/login.html', ctx)