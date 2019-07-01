from django.db import models
from django.contrib.auth.models import AbstractUser


class Tag(models.Model):
    name = models.CharField(max_length=120, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"self.name"


class Keyword(models.Model):
    name = models.CharField(max_length=120, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"self.name"


class Author(AbstractUser):
    date_of_birth = models.DateField()

    def __str__(self):
        return f"self.name"


class Document(models.Model):
    name = models.CharField(max_length=120, blank=True)
    file_path = models.FilePathField()
    file_type = models.CharField(max_length=20)
    keywords = models.ManyToManyField(Keyword)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    word_art = models.FilePathField()
    contents = models.CharField(max_length=255)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"self.name"
