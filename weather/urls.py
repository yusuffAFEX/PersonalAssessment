from django.urls import path
from . import views

app_name = 'weather'

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('form/', views.VisitorFormView.as_view(), name='form'),
    path('list/', views.LocationListView.as_view(), name='location-list'),
    path('location/<str:location>/', views.LocationDetailView.as_view(), name='details'),
    path('user/<int:pk>/', views.SubscribeUnsubscribeView.as_view(), name='subscribe-and-unsubscribed'),
]
