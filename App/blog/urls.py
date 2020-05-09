from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blog, name = "blog"),
    # path('<int:carlist_id>', views.single, name = "single")
]