from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,"main/index.html")

def about(request):
    return render(request,"main/about.html")

def new_url(request):
    return HttpResponse("<h1>New URL</h1>")

def new_page(request):
    return render(request, "main/new_page.html")
