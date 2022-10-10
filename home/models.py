"""
Program Logic
"""

#from pyexpat import model
from django.db import models
import pandas as pd
#from sqlalchemy import case, column
import haversine as hs
# Create your models here.

# models needed:

# TODO: Bundling of a django project
# TODO: Hosting the application
# ! Find out how much carbon kills 1 animal above


CITY_LIST = pd.read_excel("./home/static/home/data_files/worldcities.xlsx")

MyList = CITY_LIST[['city', 'city_ascii', 'lat', 'lng']]
LatLon = CITY_LIST[['lat', 'lng']]

MyList2 = MyList.values.tolist()
MyList3 = LatLon.values.tolist()


class Calculator(models.Model):
    """
    Class calculator class
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
