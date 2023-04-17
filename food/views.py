from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Pie, Cake, Donut, Order, Item, Itemm
from django.contrib.auth.forms import UserCreationForm
from .forms import NewUserForm, ItemForm
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
import random
import json


def randomOrderNumber(length):
    sample = 'ABCDE123456789'
    numberO = ''.join(random.choice(sample) for i in range(length))
    return numberO


def index(request):
    request.session.set_expiry(0)
    items = Itemm.objects.all()
    ctx = {'items': items}
    return render(request, "food/index.html", ctx)


def menu(request):
    request.session.set_expiry(0)
    return render(request, "food/menu.html")    


def add_item(request):
    request.session.set_expiry(0)
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    form = ItemForm()
    ctx = {'form': form}    
    return render(request, "food/add-item.html", ctx)


def edit_item(request, itemm_id):
    item = get_object_or_404(Itemm, id=itemm_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
        return redirect('index')
    form = ItemForm(instance=item)
    ctx = {'form': form}    
    return render(request, 'food/edit.html', ctx)   


def delete_item(request, itemm_id):
    item = get_object_or_404(Itemm, id=itemm_id)
    item.delete()
    return redirect('index')    


def pie(request):
    request.session.set_expiry(0)
    pies = Pie.objects.all()
    ctx = {'pies': pies}
    print(pies)
    return render(request, "food/pies.html", ctx)


def cakes(request):
    request.session.set_expiry(0)
    cakes = Cake.objects.all()
    ctx = {'cakes': cakes}
    print(cakes)
    return render(request, "food/cakes.html", ctx)


def donut(request):
    request.session.set_expiry(0)
    donuts = Donut.objects.all()
    ctx = {'donuts': donuts}
    print(donuts)
    return render(request, "food/donuts.html", ctx)


@csrf_exempt
def order(request):
    request.session.set_expiry(0)
    if request:
        request.session['note'] = request.POST.get('note')
        request.session['order'] = request.POST.get('orders')      
    ctx = {'active_link': 'order-list'}
    return render(request, "food/order-list.html", ctx)


def susscess(request):
    request.session.set_expiry(0)
    order = request.session['order']
    ctx = {'order': order}
    return render(request, 'food/susscess.html', ctx)    


def signup(request):
    request.session.set_expiry(0)
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
    request.session.set_expiry(0)
    if request.POST:
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(request, username='username', password='pwd')
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username and/or password are not correct')
        print("Email:", username)
        print("Password:", pwd)
    ctx = {'active_link': 'login'}
    return render(request, 'food/login.html', ctx)


def logOut(request):
    logout(request)
    return redirect('index')
    