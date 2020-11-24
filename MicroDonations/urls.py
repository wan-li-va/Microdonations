# <!-- /***************************************************************************************
# *  REFERENCES
# *  Title: In 5 mins: Set up Google login to sign up users on Django
# *  Author: Zoe Chew
# *  Date: July 27 2019
# *  Code version: 1.0
# *  URL: https://whizzoe.medium.com/in-5-mins-set-up-google-login-to-sign-up-users-on-django-e71d5c38f5d5
# *  Software License: N/A
# ***************************************************************************************/ -->

# """MicroDonations URL Configuration

from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView  # <--

from donations import views
from . import views as viewsMicroDonations

urlpatterns = [
    path('', views.index, name='index'),
    path('login',
         TemplateView.as_view(template_name="donations/login.html"), name="login"),  # <--
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # <--
    path('donations/', include('donations.urls')),
    path('logout/', viewsMicroDonations.logout_view),

]
