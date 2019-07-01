from django.test import TestCase
from .models import Tag


class TagTestCase(TestCase):
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
