"""oblivious_restaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from food.views import index, pie, cakes, donut, order, signup, logIn

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index_page"),
    path('pie.html', pie, name='pie_page'),
    path('cakes.html', cakes, name="cakes_page"),
    path('donuts.html', donut, name="donuts_page"),
    path('order-list.html', order, name="orders-page"),
    path('signup.html', signup, name="signup-page"),
    path('login.html', logIn, name="logIn-page"),
    path('index.html', index, name="index"),
    
]
