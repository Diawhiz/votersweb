from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic

# Create your views here.
def(request):
    return render(request, 'base/home.html')