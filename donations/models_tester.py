from django.test import TestCase

from donations.models import Organization
from donations.models import Task

class OrganizationModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Organization.objects.create(organization_text='OrganizationText', description_text='DescriptionText')

    def test_organization_text(self):
        organization_actual = Organization.objects.get(id=1)
        organization_expected = organization_actual._meta.get_field('organization_text').verbose_name
        self.assertEqual(organization_actual, organization_expected)

    def test_description_text(self):
        description_actual = Organization.objects.get(id=1)
        description_expected = description_actual._meta.get_field('description_text').verbose_name
        self.assertEqual(description_actual, description_expected)
    
 