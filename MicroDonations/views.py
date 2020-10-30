from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
