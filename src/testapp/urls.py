"""URLS for Testapp"""
from django.urls import path
from .views import pong

urlpatterns = [path("ping/", pong, name="ping")]
