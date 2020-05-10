from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from cars.models import CarsList
from .models import Blog
from contacts.models import Contacts
from carmanager.models import CarManager
from django.contrib import messages, auth
from django.contrib.auth.models import User


def blog(request):
    # blog_list = carlist
    blog_list = CarsList.objects.all()
    order = Contacts.objects.distinct("car_id")   

    context = {
        "order": order,
        "blog_list": blog_list,
        "title": "Blog-articles",
        "subtitle": "Lorem ipsum dolor sit amet consectetur adipisicing elit."
    }    
    return render(request, 'blog/blog.html', context)

def comment(request):
    # if request.method == "POST":
    #     user_id = request.POST['user_id']
    return render(request, 'blog/comment.html')


# def single(request):
#     blog_car = get_object_or_404(CarsList)
#     blog_manager = get_object_or_404(CarManager, name=blog_car.carmanager)
#     context = {
#         "blog_car": blog_car,
#         'title': "Single Blog Posts Title",
#         "blog_manager": blog_manager
#     }
    
#     return render(request, 'blog/single.html', context)

