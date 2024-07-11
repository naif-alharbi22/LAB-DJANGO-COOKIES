from . import views
from django.urls import path


NameApps='WebsiteHome'


urlpatterns=[
    path('' , views.HomePages , name='HomePages'),
    path('properties/', views.properties, name='properties'),
    path('contact/' , views.contact , name='contact'),
    path('mode/dark/' , views.dark_mode , name='dark'),
    path('mode/light' , views.light_mode , name='light'),
]
