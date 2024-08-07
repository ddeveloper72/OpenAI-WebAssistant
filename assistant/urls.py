""" Description: This file contains the URL patterns for the assistant app."""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('error', views.error_handler, name='error_handler'),
]