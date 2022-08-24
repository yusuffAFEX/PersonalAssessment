import requests
from django.conf import settings
from django.shortcuts import render

# Create your views here.
from weather.models import Location
from ipware import get_client_ip
from ip2geotools.databases.noncommercial import DbIpCity


def index(request):

    result = get_client_ip(request)
    # try:
    #     response = DbIpCity.get(result[0], api_key="free")
    # except Exception:
    #     response = "Unknown"
    # print(response)
    ip_data = requests.get("https://api.ipify.org?format=json").json()
    load_data = requests.get("http://ip-api.com/json/" + ip_data['ip']).json()
    if request.method == "GET":
        location = request.GET.get('location')
        if location:
            locations = Location.objects.filter(name__iexact=location)
        else:
            locations = Location.objects.all()[:2]
    return render(request, "weather/index.html", {'locations': locations,
                                                  'load_data': load_data,
                                                  'ip_data': ip_data})


def details(request, location):
    try:
        api = requests.get(
            "http://api.openweathermap.org/data/2.5/weather?q=" + location + ",nigeria&APPID=4c742b12a83585de3f10066724cd3d85").json()
    except Exception:
        api = "Error..."

    weather = {
        'city': location,
        'temperature': api['main']['temp'],
        'description': api['weather'][0]['description']
    }

    return render(request, "weather/detail.html", {'api': api, 'weather': weather})
