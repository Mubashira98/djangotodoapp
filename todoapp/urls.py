from django.contrib import admin
from django.urls import path, include

from todoapp import views

urlpatterns = [
    path('',views.mainpage,name='mainpage'),
    ]