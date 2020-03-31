from django.shortcuts import render

def index(request):
    return render(request, 'carlist/carlist.html')

def singlecar(request):
    return render(request, 'carlist/singlecar.html')


