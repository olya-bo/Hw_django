from django.db import models
from django.conf import settings


class Author(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=120)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return f'{self.name} - {", ".join(i.name for i in self.authors.all())}'


class InstanceBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    took_book = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id} - {self.book}"


