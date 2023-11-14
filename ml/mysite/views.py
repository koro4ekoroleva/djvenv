from django.shortcuts import render
from django.http import HttpResponse


def handle_uploaded_file(f):
    with open(f"model/imgs/{f.name}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def index(request):
    if request.method == "post":
        pass
    return render(request, 'index.html')


def about_me(request):
    return render(request, "about_me.html")

def nyan_cat(request):
    return HttpResponse("NYA!")