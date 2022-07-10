from pyexpat import model
from django.db import models
from django.forms import ModelForm, modelform_factory
import pandas as pd
from sqlalchemy import column
# Create your models here.

# models needed:
    # // 1. a model that fetches the cities from the .csv/.excel file and populates the view -> template -> form with it: pandas
    # ? Check if modelForm fields can have widget=forms.Select(choices=xyz) so as to replece forms.py with a model here
    # TODO: 2. Fetch data from the form selection (after submission) and use it to calculate:
    #     ! a. Distance between the 2 points
    #     ! b. Carbon footprint
    # 3. Modified view/template (perhaps through a model) so as to display the result


CITY_LIST = pd.read_excel("./home/static/home/data_files/worldcities.xlsx")

MyList = CITY_LIST[['city', 'city_ascii']]
LatLon = CITY_LIST[['lat', 'lng']]

MyList2 = MyList.values.tolist()
MyList3 = LatLon.values.tolist()

class Calculator(models.Model):
    """
    // My calculator model from which I'll derive the form
    // Fields from the csv using panda
    Distance & carbon methods
    Result method
    """

    dep_city = models.CharField(max_length=50, null=False)
    des_city = models.CharField(max_length=50, null=False)
    dep_latitude = models.IntegerField()
    des_longitude = models.IntegerField()
