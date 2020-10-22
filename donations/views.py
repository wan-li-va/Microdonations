from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from .models import Organization, Task

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
    list_of_organizations = Organization.objects.all()
    template = loader.get_template('donations/listofdonations.html')
    context = {
        'list_of_organizations': list_of_organizations,
    }
    return HttpResponse(template.render(context, request))

def tasks(request):
    list_of_tasks = Task.objects.all()
    template = loader.get_template('donations/listoftasks.html')
    context = {
        'list_of_tasks': list_of_tasks,
    }
    return HttpResponse(template.render(context, request))

def organization_form(request):
    template = loader.get_template('donations/add_organization_form.html')
    context = {}
    return HttpResponse(template.render(context, request))

