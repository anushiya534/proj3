"""library URL Configuration

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
from django.urls import include,path
from FirstApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('login',views.login,name="login"),
    path('registration',views.registration,name="registration"),
    path('home',views.home,name="home"),
    path('Artist',views.Artist,name="Artist"),
    path('contact',views.contact,name="contact"),
    path('submit',views.submit,name="submit"),
    path('buy',views.buy,name="buy"),
    path('buy1',views.buy1,name="buy1"),
    path('buy2',views.buy2,name="buy2"),
    path('order',views.order,name="order"),
    path('order1',views.order1,name="order1"),
    path('order2',views.order2,name="order2")

]
