from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task_2
from .forms import Task_2_Form
from .forms import CommentForm
from .models import Comment

def index(request):
    tasks = Task_2.objects.order_by("-id")
    return render(request,"main/index.html", {'title':"Главная страница", 'tasks':tasks})

def about(request):
    return render(request,"main/about.html")

def new_url(request):
    return HttpResponse("<h1>New URL</h1>")

def new_page(request):
    comments = Comment.objects.all()
    form = CommentForm()
    context = {
        'form': form
    }
    return render(request, "main/new_page.html", context)#, {'title':"Новая страница", "comments":comments})

def create(request):
    error = ''
    if request.method == 'POST':
        form = Task_2_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'форма была не верной'
    form = Task_2_Form()
    context = {
        'form':form,
        'error':error
    }
    return render(request, "main/create.html", context)
