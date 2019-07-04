from django.db import models
from django.contrib.auth.models import AbstractUser


class Tag(models.Model):
    name = models.CharField(max_length=120, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Keyword(models.Model):
    name = models.CharField(max_length=120, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Author(AbstractUser):
    def __str__(self):
        return self.username


class Document(models.Model):
    name = models.CharField(max_length=120, blank=True)
    file_content = models.FileField(null=True, blank=True)
    keywords = models.ManyToManyField(
        Keyword, null=True, blank=True, default=False)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, default=False, null=True, blank=True)
    word_art = models.ImageField(null=True, blank=True)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
