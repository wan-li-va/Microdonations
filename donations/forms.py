from django.forms import ModelForm
from .models import Profile
from django.contrib.auth.models import User


# class ProfileForm(ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['profile_bio']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_bio', 'profile_location', 'profile_phone')
