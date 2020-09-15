from django.contrib import admin
from django.urls import path
from django.conf.urls import handler400, handler500
from . import views

app_name = "career"
urlpatterns = [
    path('resource/', views.resource, name='resource'),
]
