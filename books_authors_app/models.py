from django.db import models

# Create your models here.


class Books(models.Model):
    title = models.CharField(max_length=255)
    describe = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Authors(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    book = models.ManyToManyField(Books, related_name="authors")
    notes = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
