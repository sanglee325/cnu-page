from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'main/index.html', {'index': index})

def about(request):
    return render(request, 'main/about.html', {'about': about})

def manage(request):
    return render(request, 'main/building.html', {'manage': manage}) 

def contact(request):
    return render(request, 'main/building.html', {'contact': contact})