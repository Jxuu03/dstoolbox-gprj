from django.contrib import admin
from django.urls import path,include
from matplotlibapp.views import *

urlpatterns = [
    path('',home,name='home'),
    path('top_5/',top_5,name='top_5'),
    path('pie',pie,name='pie')
]
