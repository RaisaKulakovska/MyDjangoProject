from django.shortcuts import render

# Create your views here.
def blog(request):
    data = {'title': "Car Articles"}
    return render(request, 'blog/blog.html', data)

def single(request):
    data = {'title': "Single Blog Posts Title"}
    return render(request, 'blog/single.html', data)

