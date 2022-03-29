
from argparse import Namespace
from turtle import home
from django.urls import path
from .views import homePage

app_name='musics'

urlpatterns = [
    
    path('',homePage,name='home_page')   
]
