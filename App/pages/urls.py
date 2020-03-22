from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name = "about"),
    path('services', views.services, name = "services"),
    path('contactus', views.contact, name = "contact")
]
