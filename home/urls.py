from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    # path('', views.calculator, name='calculator'),
    # path('calculator/', views.calculator, name='calculator'),
    path('form', views.get_cities, name='cities'),
]
