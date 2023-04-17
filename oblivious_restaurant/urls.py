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
from food import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index_page"),
    path('pie.html', views.pie, name='pie_page'),
    path('cakes.html', views.cakes, name="cakes_page"),
    path('donuts.html', views.donut, name="donuts_page"),
    path('menu.html', views.menu, name="menu_page"),
    path('order-list.html', views.order, name="orders-page"),
    path('signup.html', views.signup, name="signup-page"),
    path('login.html', views.signInView, name="signin-page"),
    path('logout.html', views.logOut, name="logout-page"),
    path('susscess.html', views.susscess, name="susscess-page"),
    path('add-item.html', views.add_item, name="add-item-page"),
    path('edit/<itemm_id>', views.edit_item, name="edit-item-page"),
    path('delete/<itemm_id>', views.delete_item, name="delete-item-page"),
    path('index.html', views.index, name="index"),
    path('pie.html', views.pie, name='pie_page'),
    
]
