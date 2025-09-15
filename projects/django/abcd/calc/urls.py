from django.urls import path
from . import views
from django.contrib import admin
from calc.views import home


urlpatterns=[
    path('',home,name='home')
]