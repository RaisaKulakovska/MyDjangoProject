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
    blog_list = Blog.objects.all().filter(is_published=True)  
    manager_all = CarManager.objects.all().filter(is_published=True)

    paginator = Paginator(blog_list, 3)
    page = request.GET.get("page")
    paged_bloglist = paginator.get_page(page)

    context = {        
        "blog_list": blog_list,
        'manager_all':manager_all,
        "title": "Blog-articles",
        "subtitle": "Blog lorem ipsum dolor sit amet consectetur adipisicing elit."
    } 
    
    return render(request, 'blog/single.html', context)   

def single(request, blog_list_id):
    blog_item = get_object_or_404(Blog, pk=blog_list_id)
    blog_manager = get_object_or_404(CarManager, name=blog_item.blog_manager)
    
    context = {        
        "blog_item": blog_item,
        'blog_manager':blog_manager,
    }
    
    return render(request, 'blog/single.html', context)

