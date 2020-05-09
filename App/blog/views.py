from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from cars.models import CarsList
from .models import Blog


def blog(request):
    # blog_list = carlist
    blog_list = CarsList.objects.all().filter(is_published=True)

    paginator = Paginator(blog_list, 6)
    page = request.GET.get("page")
    paged_bloglist = paginator.get_page(page)

    context = {
        "blog_list": paged_bloglist,
        "title": "Blog-articles",
        "subtitle": "Lorem ipsum dolor sit amet consectetur adipisicing elit."
    }    
    return render(request, 'blog/blog.html', context)

# def single(request):
#     blog_car = get_object_or_404(CarsList, pk=carlist_id)
#     blog_manager = get_object_or_404(CarManager, name=blog_car.carmanager)
#     context = {
#         "blog_car": blog_car,
#         'title': "Single Blog Posts Title",
#         "blog_manager": blog_manager
#     }
    
#     return render(request, 'blog/single.html', context)

