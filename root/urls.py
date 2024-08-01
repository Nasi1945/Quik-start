from django.urls import path
from .views import *

app_name = 'root'

urlpatterns = [
    path('' , home, name='home'),
    path('#about', about, name='about'),
    path('#features', features, name='features'),
    path('#services', services, name='services'),
    path('#pricing', pricing , name='pricing'),
    path('#contact', contact, name='contact')
]
