from django.contrib import admin
from django.urls import path
from .views import *
app_nem = 'User'
urlpatterns = [
    path('', login, name='login'),
    path('register/', register, name="register"),
]
