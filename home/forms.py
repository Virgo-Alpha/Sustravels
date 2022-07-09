from random import choices
from django import forms
import pandas as pd

# create your forms here
# TODO 1: Populate the dropdown with data from the .xlsx file
#   ! - Turn to dict
#   ?? How to turn a dataframe into a tuple (or list of items that can be iterated over) - Check Sololearn Python
#   ? Turn the dataframe into tuples of 2 separated by commas
#   ! - Iterate using for to get the tuples.
#   ! - Populate the MyCities (choices) tuple with data from the iteration

# CITY_LIST = pd.read_excel("./home/static/home/data_files/worldcities.xlsx")

# list1 = dict(CITY_LIST[['city']])
# list2 = dict(CITY_LIST[['city_ascii']])


# for row in CITY_LIST.to_dict('records'):
#     x = row[['city']]
#     y = row[['city_ascii']]

# MyTuple = (x, y)

# MyTuple = tuple(CITY_LIST[['city', 'city_ascii']].to_dict('list'))


MyCities = (
        # (list2['city_ascii'], list1['city']),
        ('x', 'y'),
        ('a', 'b') # ! Change this so that b is a city name, a can be an index -> dict(CITY_LIST[['city']]) is displayed this way; Check dict datatype
)


class CalculatorForm(forms.Form):
    dep_city = forms.CharField(label='Departure Location:', widget=forms.Select(choices=MyCities))
    des_city = forms.CharField(label='Destination location:', widget=forms.Select(choices=MyCities))
