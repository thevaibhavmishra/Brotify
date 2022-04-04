
from argparse import Namespace
from turtle import home
from django.urls import path
from .views import homePage,AddForm

app_name='musics'

urlpatterns = [
    path('',homePage,name='home_page'),
    path('add/',AddForm,name='add_page')   
]
