from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pestaña/', views.pestaña, name='pestaña'),
    path('nombreseqdoc/', views.nombreseqdoc, name='nombreseqdoc')
]