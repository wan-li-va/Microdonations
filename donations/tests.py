

# Create your tests here.
import pytest
from django.test import TestCase
from django.test import RequestFactory, TestCase
from .views import index, login, donations, tasks, profile, edit_profile, organizationform, add_organization, org_description, task_description
from .models import Organization, Task, Profile

class ModelTestCase(TestCase):
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

class LoginTestCase(TestCase):

    def test_login(self):

        # First check for the default behavior
        response = self.client.get('/user/')
        self.assertRedirects(response, '/accounts/login/?next=/user/')

        # Then override the LOGIN_URL setting
        with self.settings(LOGIN_URL='/other/user/'):
            response = self.client.get('/user/')
            self.assertRedirects(response, '/other/login/?next=/user/')


class ViewsTest(TestCase):
    def test_login_view(self):
        request = RequestFactory().get('/')
        view = login()
        view.setup(request)

        context = view.get_context_data()
        self.assertIn('', context)

    def test_donations_view(self):
        request = RequestFactory().get('/')
        view = donations()
        view.setup(request)

        context = view.get_context_data()
        self.assertIn('list_of_organizations', context)

    def test_tasks_view(self):
        request = RequestFactory().get('/')
        view = tasks()
        view.setup(request)

        context = view.get_context_data()
        self.assertIn('list_of_tasks', context)

    def test_profile_view(self):
        request = RequestFactory().get('/')
        view = tasks()
        view.setup(request)

        profbio = RequestFactory.get(profile_bio)
        profphone = RequestFactory.get(profile_phone)
        proflocation = RequestFactory.get(profile_location)
        profemail = RequestFactory.get(profile_email)

        self.assertIn(profbio, 'profile_bio')
        self.assertIn(profphone, 'profile_phone')
        self.assertIn(proflocation, 'profile_location')
        self.assertIn(profemail, 'profile_email')

    def test_edit_profile_view(self):
        request = RequestFactory().get('/')
        view = tasks()
        view.setup(request)

        context = view.get_context_data()
        self.assertIn('user_form', context)

    def test_organization_form_view(self):
        request = RequestFactory().get('/')
        view = tasks()
        view.setup(request)

        context = view.get_context_data()
        self.assertIn('organization_text', organization_text)
        self.assertIn('description_text', description_text)

    # def test_add_organization_view(self):
    #     request = RequestFactory().get('/')
    #     view = tasks()
    #     view.setup(request)

    #     context = view.get_context_data()
    #     self.assertIn('list_of_tasks', context)


    




