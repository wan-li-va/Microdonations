from django.db import models

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
