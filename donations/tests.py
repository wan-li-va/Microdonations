

# Create your tests here.
from django.test import TestCase
from django.test import RequestFactory, TestCase
from .views import index, login, donations, tasks, profile, edit_profile, organizationform, add_organization, org_description, task_description
from .models import Organization, Task, Profile
from django.urls import reverse
from donations.forms import ProfileForm, UserForm
from django.test import Client


class OrganizationModelTest(TestCase):
    def setUp(self):
        Organization.organization_text = 'organization_text'
        Organization.description_text = 'description_text'
        Organization.fundsRaised = 500
        Organization.fundsGoal = 1000
        Organization.is_spotlighted = True

    def test_organization_text(self):
        #organization_text = Organization.objects.get(organization_text="a")
        self.assertEqual(Organization.organization_text, "organization_text")
        self.assertEqual(Organization.description_text, 'description_text')

    def test_organization_funds(self):
        self.assertEqual(Organization.fundsRaised, 500)

    def test_organization_funds_goal(self):
        self.assertEqual(Organization.fundsGoal, 1000)

    def test_organization_isSpotlighted(self):
        self.assertTrue(Organization.is_spotlighted)


class TaskModelTest(TestCase):
    def setUp(self):
        Task.task_text = 'task_text'
        Task.description_text = 'description_text'
        Task.is_done = True

    def test_organization_isSpotlighted(self):
        self.assertTrue(Organization.is_spotlighted)

    def test_task_text(self):
        self.assertEqual(Task.task_text, "task_text")
        self.assertEqual(Task.description_text, "description_text")

    def test_task_isDone(self):
        self.assertTrue(Task.is_done)


class ProfileModelTest(TestCase):
    def setUp(self):
        Profile.profile_bio = "profile_bio"
        Profile.profile_location = "profile_location"
        Profile.profile_phone = "profile_phone"
        Profile.totalDonated = 400

    def test_profile_text(self):
        self.assertEqual(Profile.profile_bio, "profile_bio")
        self.assertEqual(Profile.profile_location, "profile_location")
        self.assertEqual(Profile.profile_phone, "profile_phone")

    def test_profile_totalDonated(self):
        self.assertEqual(Profile.totalDonated, 400)


class ProfFormTest(TestCase):

    def test_valid_profile_form(self):
        form = ProfileForm(data={'profile_bio': "profile_bio", 'profile_location': "profile_location",
                                 'profile_bio': "profile_bio", 'profile_phone': '1234567890'})
        self.assertTrue(form.is_valid())

    def test_invalid_profile_form(self):
        form = ProfileForm(data={'profile_bio': "profile_bio",
                                 'profile_location': "profile_location", 'profile_bio': "profile_bio"})
        self.assertFalse(form.is_valid())


class UserFormTest(TestCase):

    def test_valid_user_form(self):
        form = UserForm(data={'first_name': 'first_name',
                              'last_name': 'last_name'})
        self.assertTrue(form.is_valid())

    def test_invalid_user_form(self):
        form = UserForm(data={'first_name': 'first_name', 'last_name': ''})
        self.assertTrue(form.is_valid())


# class LoginTestCase(TestCase):
#     def test_login(self):

#         # First check for the default behavior
#         response = self.client.get('/user/')
#         self.assertRedirects(response, '/accounts/login/?next=/user/')

#         # Then override the LOGIN_URL setting
#         with self.settings(LOGIN_URL='/other/user/'):
#             response = self.client.get('/user/')
#             self.assertRedirects(response, '/other/login/?next=/user/')

class ViewsTest(TestCase):
    def test_index(self):
        response = self.client.get(reverse('donations:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'donations/index.html')

    # def test_login(self):
    #     response = self.client.get(reverse('donations:login'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'donations/login.html')

    def test_donationslist(self):
        response = self.client.get(reverse('donations:donations'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'donations/listofdonations.html')

    def test_taskslist(self):
        response = self.client.get(reverse('donations:tasks'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'donations/listoftasks.html')

    def test_profile_page(self):
        response = self.client.get(reverse('donations:profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'donations/profile.html')

    def test_leaderboard_page(self):
        response = self.client.get(reverse('donations:leaderboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'donations/leaderboard.html')

    def test_contact_page(self):
        response = self.client.get(reverse('donations:contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'donations/contact.html')
