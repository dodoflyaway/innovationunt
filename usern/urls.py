from django.contrib import admin
from django.urls import path
from django.urls import include
from .import views

urlpatterns = [
   
    path("signupn/",views.signupn,name="signupn"),
    path("loginn/",views.loginn,name="loginn"),
    path('',include("innovator.urls")),
]
