from django.db import models


# Create your models here.


class Location(models.Model):
    visitor = models.ForeignKey('Visitor', on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name.capitalize()


class Visitor(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
