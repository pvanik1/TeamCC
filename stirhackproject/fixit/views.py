from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'fixit/base.html')


def about(request):
    return render(request, 'fixit/about.html')