from django.urls import path
from .views import *

urlpatterns = [
    path('', MainView, name = 'main'),
    path('contact/', ContactView, name='contact'),
]