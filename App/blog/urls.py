from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blog, name = "blog"),
    path('single', views.single, name = "single")
]