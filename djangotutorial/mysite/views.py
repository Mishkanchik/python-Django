from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

