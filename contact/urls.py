from django.urls import path
from . import views

""" url paths. """
urlpatterns = [
    path('', views.contact, name='contact'),
]