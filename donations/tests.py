# Create your tests here.
import pytest
from django.test import TestCase

from .models import Organization, Task, Profile

class OrganizationTestCase(TestCase):
    def setUp(self):
        #Organization.objects.create(organization_text="a", description_text="b")
        Organization.organization_text = 'organization_text'
        Organization.description_text = 'description_text'

        Task.task_text = 'task_text'
        Task.description_text = 'description_text'

        Profile.profile_bio = "profile_bio"
        Profile.profile_location = "profile_location"
        Profile.profile_phone = "profile_phone"

    def test_organization_model(self):
        #organization_text = Organization.objects.get(organization_text="a")
        self.assertEqual(Organization.organization_text, "organization_text")
        self.assertEqual(Organization.description_text, 'description_text')

    def test_task_model(self):
        self.assertEqual(Task.task_text, "task_text")
        self.assertEqual(Task.description_text, "description_text")

    def test_profile_model(self):
        self.assertEqual(Profile.profile_bio, "profile_bio")
        self.assertEqual(Profile.profile_location, "profile_location")
        self.assertEqual(Profile.profile_phone, "profile_phone")
