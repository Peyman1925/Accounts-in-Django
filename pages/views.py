from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def home(request):
    return render(request, 'home.html')
