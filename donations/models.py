from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Organization(models.Model):
    organization_text = models.CharField(max_length=200)
    description_text = models.CharField(max_length=200)

    def __str__(self):
        return self.organization_text


class Task(models.Model):
    task_text = models.CharField(max_length=200)
    description_text = models.CharField(max_length=200)

    def __str__(self):
        return self.task_text
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_bio = models.CharField(max_length=500)
    profile_location = models.CharField(max_length=100)
    profile_phone = models.CharField(max_length=100)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
