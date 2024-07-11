from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.

def HomePages(HttpRequest:HttpRequest):

    return render(HttpRequest, 'main/index.html')

def properties(HttpRequest:HttpRequest):
    return render(HttpRequest , 'main/nsf.html')