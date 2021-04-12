from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('automatic_crud/',include('automatic_crud.urls')),
]
