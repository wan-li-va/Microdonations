from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
from django.utils import timezone


class Organization(models.Model):
    organization_text = models.CharField(max_length=200)
    description_text = models.CharField(max_length=200)
    fundsRaised = models.FloatField(null=True, blank=True, default=0.0)
    fundsGoal = models.FloatField(null=True, blank=True, default=0.0)

    def __str__(self):
        return self.organization_text


class Task(models.Model):
    task_text = models.CharField(max_length=200)
    description_text = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)
    task_owner = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.task_text
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_bio = models.CharField(max_length=500)
    profile_location = models.CharField(max_length=100)
    profile_phone = models.CharField(max_length=100)
    # favorite_orgs = models.ManyToManyField(Organization)
    # image = models.ImageField(upload_to='profile_image', blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


"""
class Review(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    review_text = models.CharField(max_length=200000)
    pub_date = models.DateTimeField('date published') # auto_now_add=True
    def __str__(self):
        return self.review_text
"""
