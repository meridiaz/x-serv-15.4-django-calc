from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('<str:func>/<str:op1>/<str:op2>', views.calcular),
]
