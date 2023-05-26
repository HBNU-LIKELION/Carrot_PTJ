from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')
