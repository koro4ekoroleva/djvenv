from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('nyan_cat/', views.nyan_cat),
    path('me/', views.me)
]