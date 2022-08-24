from django.contrib import admin

# Register your models here.
from weather.models import Location, Visitor

admin.site.register(Location)
admin.site.register(Visitor)