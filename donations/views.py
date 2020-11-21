from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.urls import reverse
from .models import Organization, Task
from django.shortcuts import get_object_or_404  # used for shortcut method
from .models import Profile
from .forms import ProfileForm
from .forms import UserForm
import json
from django.core.mail import send_mail

# Create your views here.


def index(request):
    context = {}
    return render(request, 'donations/index.html', context)


def login(request):
    context = {}
    return HttpResponse(template.render(context, request))


def donations(request):
    list_of_organizations = Organization.objects.all()
    list_length = len(list_of_organizations)
    template = loader.get_template('donations/listofdonations.html')
    context = {
        'list_of_organizations': list_of_organizations, 'list_length': list_length
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


def done_task(request, pk):
    if request.method == 'POST':
        task = Task.objects.get(id=pk)
        task.is_done = True
        task.save()
        send_mail(
            'MicroDonations Task Complete :)',
            'Your task was completed by ' + request.user.first_name + '!',
            'cs3240project218@gmail.com',
            [task.task_owner.email],
            fail_silently=True,
        )
    context = {
        'list_of_tasks': Task.objects.all()
    }

    return HttpResponseRedirect(reverse('donations:tasks'))


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
        organization_img_link = request.POST['img_link']
        total = request.POST['total']
        o = Organization(organization_text=organization_text,
                         description_text=description_text, fundsGoal=total, organization_img_link=organization_img_link)
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
        t = Task(task_text=task_text,
                 description_text=description_text, task_owner=request.user)  # for sending emails
        # t = Task(task_text=task_text,
        #          description_text=description_text)   #for not sending emails
        t.save()
    return HttpResponseRedirect(reverse('donations:tasks'))


def add_fav_org(request, pk):
    if request.method == 'POST':
        org = Organization.objects.get(id=pk)
        u = request.user
        u.profile.favorite_orgs.add(org)
    return HttpResponseRedirect(reverse('donations:donations'))


def del_fav_org(request, pk):
    if request.method == 'POST':
        print("hereeeeeeeeeeeeeeeeeeeeeeee")
        org = Organization.objects.get(id=pk)
        u = request.user
        u.profile.favorite_orgs.remove(org)
    return HttpResponseRedirect(reverse('donations:donations'))


def fav_orgs(request):
    u = request.user
    list_of_organizations = u.profile.favorite_orgs.all()
    list_length = len(list_of_organizations)
    template = loader.get_template('donations/fav_orgs.html')
    context = {
        'list_of_organizations': list_of_organizations, 'list_length': list_length
    }
    return HttpResponse(template.render(context, request))


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


def checkout(request, pk):
    org = Organization.objects.get(id=pk)
    context = {'org': org}
    return render(request, 'donations/checkout.html', context)


def paymentComplete(request):
    body = json.loads(request.body)
    org = Organization.objects.get(id=body['productId'])
    org.fundsRaised += float(body['amount'])
    org.save()

    # return JsonResponse('Payment completed!', safe=False)
    # return HttpResponseRedirect(reverse('donations:tasks'))


def simpleCheckout(request):
    return render(request, 'donations/simple_checkout.html')


def org_description(request, pk):
    org = Organization.objects.get(id=pk)
    context = {
        'org': org,
    }
    return render(request, 'donations/org_description.html', context)


def task_description(request, pk):
    task = Task.objects.get(id=pk)
    context = {
        'task': task,
    }
    return render(request, 'donations/task_description.html', context)
