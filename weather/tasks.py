import requests
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.utils.safestring import mark_safe

from WeatherApp.celery import app
from weather.models import Visitor


@app.task(bind=True, ignore_result=True)
def my_scheduled_job(self):
    email_from = settings.EMAIL_HOST_USER
    visitors = Visitor.objects.all()
    for visitor in visitors:
        try:
            data = requests.get("http://api.openweathermap.org/data/2.5/weather?q=" + str(visitor.location) + ",nigeria&APPID=4c742b12a83585de3f10066724cd3d85").json()
        except Exception as e:
            return e
        weather_city = data['name']
        weather_temp = data['main']['temp']
        weather_desc = data['weather'][0]['description']
        subject = f'Current Weather Information in {weather_city}'
        message = f'Hi, Currently temperature is {weather_temp} and description is {weather_desc}. Click on the link to stop the notification..http://127.0.0.1:8000/user/{visitor.id}'
        if visitor.location:
            if visitor.is_subscribed:
                send_mail(subject, message, email_from, recipient_list=[visitor.email, ],)


