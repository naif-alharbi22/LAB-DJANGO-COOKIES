from . import views
from django.urls import path


NameApps='WebsiteHome'


urlpatterns=[
    path('' , views.HomePages , name='HomePages'),
]
