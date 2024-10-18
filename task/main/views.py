from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def car(request):
    return render(request, 'main/car.html')


def sub(request):
    return render(request, 'main/sub.html')
