from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blog, name = "blog_list"),
    path('<int:blog_id>', views.single, name = "single")
]