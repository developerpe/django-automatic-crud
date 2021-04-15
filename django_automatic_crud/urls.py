from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/',admin.site.urls),
    path('automatic_crud/',include('automatic_crud.urls')),
]
