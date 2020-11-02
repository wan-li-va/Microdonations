from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Organization, Task
from django.shortcuts import get_object_or_404  # used for shortcut method
from .models import Profile
from .forms import ProfileForm
from .forms import UserForm

# Create your views here.


def index(request):
    context = {}
    return render(request, 'donations/index.html', context)


def login(request):
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
    return render(request, 'donations/googlelogin.html', context)


def profile(request):
    if request.user.is_authenticated:
        profile_bio = request.user.profile.profile_bio
        profile_phone = request.user.profile.profile_phone
        profile_location = request.user.profile.profile_location
        profile_email = request.user.email

        context = {'profile_bio': profile_bio, 'profile_phone': profile_phone,
                   'profile_location': profile_location, 'profile_email': profile_email}
    else:
        context = {}
    return render(request, 'donations/profile.html', context)


def edit_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid() and user_form.is_valid():
            user_form.save()
            form.save()
            return redirect('/donations/profile')
    else:
        user_form = UserForm(instance=request.user)
        form = ProfileForm(instance=request.user.profile)

    context = {'user_form': user_form,
               'form': form}
    return render(request, 'donations/edit_profile.html', context)


def organizationform(request):
    template = loader.get_template('donations/add_organization_form.html')
    context = {}
    return HttpResponse(template.render(context, request))


def add_organization(request):
    if request.method == 'POST':
        organization_text = request.POST['name']
        description_text = request.POST['body']
        print(request.POST)
        o = Organization(organization_text=organization_text,
                         description_text=description_text)
        o.save()
    return HttpResponseRedirect(reverse('donations:donations'))

def taskform(request):
    template = loader.get_template('donations/add_task_form.html')
    context = {}
    return HttpResponse(template.render(context, request))

def add_task(request):
    if request.method == 'POST':
        task_text = request.POST['name']
        description_text = request.POST['body']
        print(request.POST)
        t = Task(task_text=task_text,
                description_text=description_text)
        t.save()
    return HttpResponseRedirect(reverse('donations:tasks'))
    
"""
def review(request):
    if request.method == 'POST':
        if request.POST.get('organization') and request.POST.get('review_text'):
            review=Review()
            review.organization = request.POST.get('organization')
            review.review_text = request.POST.get('review_text')
            review.save()

            return render(request, 'polls/review.html')
        else:
            return render(request, 'polls/review.html')
    else:
        return render(request, 'polls/review.html')
    
def reviewList(request):
    list_of_comments = Comment.objects.order_by('-pub_date')
    template = loader.get_template('polls/list.html')
    context = {
        'list_of_comments': list_of_comments,
    }
    return HttpResponse(template.render(context,request))
"""