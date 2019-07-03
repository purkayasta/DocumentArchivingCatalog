from django.test import TestCase, Client
from django.urls import reverse

from .models import Tag, Document


class TagModelTestCase(TestCase):
    def setUp(self):
        Tag.objects.create(name="lion")
        Tag.objects.create(name="cat")

    def test_tag_exists(self):
        """Searching with tag"""
        result = Tag.objects.get(name='lion')
        self.assertEqual(result.name, 'lion')

    def test_tag_is_not_exists(self):
        with self.assertRaises(Tag.DoesNotExist):
            Tag.objects.get(name='123')


class HomepageUrlTestCase(TestCase):
    client = Client()

    def test_index_page_load(self):
        response = client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)
