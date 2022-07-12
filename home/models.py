from pyexpat import model
from turtle import distance
from django.db import models
import pandas as pd
from sqlalchemy import case, column
import haversine as hs
# Create your models here.

# models needed:
# // 1. a model that fetches the cities from the .csv/.excel file and populates the view -> template -> form with it: pandas
# /// ? Check if modelForm fields can have widget=forms.Select(choices=xyz) so as to replece forms.py with a model here
# // TODO: 2. Fetch data from the form selection (after submission) and use it to calculate:
#     // ! a. Distance between the 2 points
#     // ! b. Carbon footprint
# // 3. Modified view/template (perhaps through a model) so as to display the result
# TODO: Bundling of a django project
# TODO: Hosting the application
# // TODO: Method for killed Big 5 animals: lion, leopard, rhino, elephant and African Buffalo
# ! Find out how much carbon kills 1 animal above
# ? Hosting on Github Pages


CITY_LIST = pd.read_excel("./home/static/home/data_files/worldcities.xlsx")

MyList = CITY_LIST[['city', 'city_ascii', 'lat', 'lng']]
LatLon = CITY_LIST[['lat', 'lng']]

MyList2 = MyList.values.tolist()
MyList3 = LatLon.values.tolist()


class Calculator(models.Model):
    """
    // My calculator model from which I'll derive the form
    // Fields from the csv using pandas
    // Distance & carbon methods
    // Result method
    """

    def calculateDistance(latitude, longitude):
        """
        Haversine formula to get the distance
        """

        distance = hs.haversine(latitude, longitude)

        return distance

    def calculateCarbon(distance):
        """
        Calculates the carbon footprint of the tourist
        A plane emmits 102 g of CO2 per km
        """

        carbon = (distance * 102)/1000

        return carbon

    def killings(carbon):
        """
        Method to demonstrate the killing of the big 5:
        Leopard: 50 
        Lion: 75
        African buffalo: 100
        Rhino: 200
        Elephant: 250
        ! Check the accuracy of the figures
        """
        Leopard = 0
        Lion = 0
        Buffalo = 0
        Rhino = 0
        Elephant = 0

        if carbon >= 250:
            while carbon >= 250:
                Elephant += 1
                carbon -= 250

        if carbon >= 200:
            while carbon >= 200:
                Rhino += 1
                carbon -= 200

        if carbon >= 100:
            while carbon >= 100:
                Buffalo += 1
                carbon -= 100

        if carbon >= 75:
            while carbon >= 75:
                Lion += 1
                carbon -= 75

        if carbon >= 50:
            while carbon >= 50:
                Leopard += 1
                carbon -= 50

        else:
            pass

        return [Leopard, Lion, Buffalo, Rhino, Elephant]
