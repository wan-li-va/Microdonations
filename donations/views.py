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
    template = loader.get_template('donations/googlelogin.html')
    context = {}
    return HttpResponse(template.render(context, request))

def donations(request):
    template = loader.get_template('donations/listofdonations.html')
    context = {}
    return HttpResponse(template.render(context, request))

def tasks(request):
    template = loader.get_template('donations/listoftasks.html')
    context = {}
    return HttpResponse(template.render(context, request))

def organization_form(request):
    template = loader.get_template('donations/add_organization_form.html')
    context = {}
    return HttpResponse(template.render(context, request))

