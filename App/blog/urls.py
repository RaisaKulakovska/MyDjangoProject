from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blog, name = "blog"),
    path('testimonials', views.testimonials, name = "testimonials"),
    path('single', views.single, name = "single")

]