from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

def index(request):
    tasks = Task.objects.all()
    return render(request,"main/index.html", {'title':"Главная страница", 'tasks':tasks})

def about(request):
    return render(request,"main/about.html")

def new_url(request):
    return HttpResponse("<h1>New URL</h1>")

def new_page(request):
    return render(request, "main/new_page.html")
