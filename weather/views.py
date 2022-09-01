import json

import requests
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy

# Create your views here.
from django.views import View
from django.views.generic import ListView, FormView

from weather.forms import VisitorForm
from weather.models import Location, Visitor


class HomeView(View):
    def get(self, request):
        return render(request, 'weather/index.html')


class LocationListView(ListView):
    model = Location
    template_name = 'weather/list.html'

    def get_queryset(self):
        search = self.request.GET.get('location')
        if search is not None:
            queryset = Location.objects.filter(name__iexact=search)
        else:
            queryset = Location.objects.all()[:5]
        return queryset


class LocationDetailView(View):
    def get(self, request, location):
        api = requests.get(
                "http://api.openweathermap.org/data/2.5/weather?q=" + location + ",nigeria&units=metric&APPID=4c742b12a83585de3f10066724cd3d85").json()

        # try:
        #     api = json.loads(api_request.content)
        #     print(api)
        # except Exception:
        #     api = "Error..."

        context = {
            'api': api,
            'city': location,
            'temperature': api["main"]["temp"],
            'description': api["weather"][0]["description"],
            'icon': api["weather"][0]["icon"],
        }

        return render(request, "weather/detail.html", context)


class VisitorFormView(FormView):
    form_class = VisitorForm
    template_name = 'weather/form.html'
    success_url = reverse_lazy('weather:index')

    def form_valid(self, form):
        super(VisitorFormView, self).form_valid(form)
        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['location']
            if Visitor.objects.filter(email=email).exists():
                messages.error(self.request, "You already have your info with us")
                return HttpResponseRedirect(reverse('weather:form'))
            else:
                location = Location.objects.create(name=name)
                visitor = Visitor.objects.create(email=email, location=location)
                visitor.save()
                messages.success(self.request, "Information saved...")
                return HttpResponseRedirect(reverse('weather:index'))


class SubscribeUnsubscribeView(View):
    def get(self, request, pk):
        visitor = Visitor.objects.get(pk=pk)
        context = {'visitor': visitor}
        return render(request, 'weather/unsubscribed.html', context)

    def post(self, request, pk):
        visitor = get_object_or_404(Visitor, pk=pk)

        visitor.is_subscribed = not visitor.is_subscribed

        visitor.save()
        return HttpResponseRedirect(reverse('weather:subscribe-and-unsubscribed', args=[pk]))
