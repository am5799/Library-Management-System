from django.db import models
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # Add more author details if needed

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Publisher(models.Model):
    publisher = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.publishere} {self.location}"
class Language(models.Model):
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.language
