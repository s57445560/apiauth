from django.conf.urls import url
from django.contrib import admin
from apiauth import views

urlpatterns = [
    url(r'host_api/',views.Host_api.as_view(),name='hostapi'),
]