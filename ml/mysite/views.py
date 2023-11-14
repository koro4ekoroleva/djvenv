from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')


def me(request):
    return render(request, "me.html")

def nyan_cat(request):
    return HttpResponse("NYA!")