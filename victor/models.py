from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name
