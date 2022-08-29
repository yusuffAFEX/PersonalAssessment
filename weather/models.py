from django.db import models


# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name.capitalize()


class Visitor(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    email = models.EmailField()
    is_subscribed = models.BooleanField(default=True)

    def __str__(self):
        return self.email
