from django.shortcuts import render , redirect
from django.http import HttpRequest
# Create your views here.

def HomePages(HttpRequest:HttpRequest):
    
    return render(HttpRequest, 'main/index.html',{'HttpRequest':HttpRequest})

def properties(HttpRequest:HttpRequest):
    properties = [
        {"title" : "Villa Modern in Malqa", "image" : "villa1.jpg"},
        {"title" : "Great home for you in Rimal", "image" : "villa2.jpg"},
        {"title" : "Villa with 8 bedrooms in Swedey", "image" : "villa3.jpg"},
        {"title" : "Amazing Villa in Hitten", "image" : "villa4.jpg"},
    ]
    return render(HttpRequest , 'main/properties.html', {'properties':properties, 'HttpRequest':HttpRequest})

def contact(HttpRequest:HttpRequest):
    return render(HttpRequest , 'main/contact.html',{'HttpRequest':HttpRequest})

def dark_mode(HttpRequest:HttpRequest):
    url_now=redirect(HttpRequest.META.get('HTTP_REFERER' , '/'))
    url_now.set_cookie('mode','dark',max_age=60*60*24)
    return url_now

def light_mode(HttpRequest:HttpRequest):
    url_now=redirect(HttpRequest.META.get('HTTP_REFERER' , '/'))
    url_now.set_cookie('mode','light' ,max_age=60*60*24)
    return url_now

