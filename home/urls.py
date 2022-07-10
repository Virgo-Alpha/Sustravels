from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('', views.calculator, name='calculator'),
    # path('calculator', views.calculator, name='calculator'),
    path('calculator/', views.get_cities, name='calculator'),    
    # path('form', views.get_cities, name='cities'),
    path('calculator/result', views.result, name='result'), # ! the action of the form is this url which is an addition to the calculator/ one above
    # ? Another view for the above url with the decision; Handling form submissions in Django
]
