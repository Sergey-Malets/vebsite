
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new_url',views.new_url),
    path('new_page',views.new_page),
]