from django.contrib import admin
from django.urls import path,include
from matplotlibapp.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',home,name='home')
]
