from django.urls import path
from django.urls import include, path
from django.views.generic import TemplateView  # <--

from . import views

app_name = 'donations'
urlpatterns = [
    path('donationslist/', views.donations, name='donations'),
    path('taskslist/', views.tasks, name="tasks"),
    path('contact/', views.contact, name="contact"),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
    path('donationslist/organizationform/',
         views.organizationform, name="organizationform"),
    path('donationslist/organizationform/add_organization',
         views.add_organization, name="add_organization"),
    path('taskslist/taskform/',
         views.taskform, name="taskform"),
    path('taskslist/taskform/add_task',
         views.add_task, name="add_task"),
    path('add_fav_org/<int:pk>/',
         views.add_fav_org, name="add_fav_org"),
    path('del_fav_org/<int:pk>/',
         views.del_fav_org, name="del_fav_org"),
    path('fav_orgs',
         views.fav_orgs, name="fav_orgs"),
    path('spotlight',
         views.spotlight, name="spotlight"),
    path('leaderboard',
         views.leaderboard, name="leaderboard"),
    path('checkout/<int:pk>/', views.checkout, name="checkout"),
    path('complete/', views.paymentComplete, name="complete"),
    path('simple-checkout/', views.simpleCheckout, name="simple-checkout"),
    path('done_task/<int:pk>/', views.done_task, name="done_task"),
    path('donationslist/orgdescription/',
         views.org_description, name='org_description'),
    path('donationslist/orgdescription/<int:pk>',
         views.org_description, name='org_description'),
    path('tasklist/taskdescription/<int:pk>',
         views.task_description, name="task_description")
]
