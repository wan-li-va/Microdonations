from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse

# Create your views here.


def index(request):
    template = loader.get_template('donations/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def login(request):
    template = loader.get_template('donations/login.html')
    context = {}
    return HttpResponse(template.render(context, request))
