from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pie, Cake, Donut, Order, Item, Review
from django.contrib.auth.forms import UserCreationForm
from .forms import NewUserForm
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
    review = Review.objects.all()
    ctx = {'review': review}
    print(review)
    return render(request, "food/index.html", ctx)


def review(request):
    if request.method == 'POST':
        reviewer = request.POST.get('item_name')
        review_area = request.POST.get('item_text')
        Review.objects.create(reviewer=reviewer, review_area=review_area)
        return redirect('index')
    return render(request, "food/add-review.html") 


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
    if request.is_ajax():
        request.session['note'] = request.POST.get('note')
        request.session['order'] = request.POST.get('orders')


        print(request.session['note'], request.session['order'])
        
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
            signInView(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username and/or password are not correct')
        print("Email:", username)
        print("Password:", pwd)
    ctx = {'active_link': 'login'}
    return render(request, 'food/login.html', ctx)


# def logOut(request):
#     request.session.set_expiry(0)
#     ctx = {'name': 'OBLIVIOUS BAKERY'}
#     return render(request, "food/logout.html", ctx)

def logOut(request):
    logout(request)
    return redirect('index')

    # if request.is_ajax():
    #     request.session.set_expiry(0)
    #     note = request.session['note'] = request.POST.get('note')
    #     orders = request.session['orders'] = request.POST.get('orders')
    #     orders = json.loads(request.session['orders'])
    #     totall = request.session['totall'] = request.POST.get('totall')
    #     if request.user.is_authenticated:
    #         order = Order(customer=request.user, number=randomOrderNumber(6), totall=float(request.session['totall']), note=request.session['note'])
    #         order.save()
    #         for article in orders:
    #             item = Item(
    #                 order=order, 
    #                 name=article[0],
    #                 price=float(article[2]),
    #                 size=article[1]
    #             )
    #             item.save()