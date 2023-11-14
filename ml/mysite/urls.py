from django.urls import path
from mysite.views import *

urlpatterns = [
    path('', index),
    path('about_me/', about_me)
]