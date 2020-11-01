from django.urls import path
from django.urls import include, path
from django.views.generic import TemplateView  # <--

from . import views

app_name = 'donations'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('donationslist/', views.donations, name='donations'),
    path('taskslist/', views.tasks, name="tasks"),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
    path('donationslist/organizationform/',
         views.organizationform, name="organizationform"),
    path('donationslist/organizationform/add_organization',
         views.add_organization, name="add_organization"),
]
