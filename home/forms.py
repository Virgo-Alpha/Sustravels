from random import choices
from django import forms
import pandas as pd

from home.models import MyList3

# create your forms here

CITY_LIST = pd.read_excel("./home/static/home/data_files/worldcities.xlsx")

MyList = CITY_LIST[['city', 'city_ascii']]


MyList2 = MyList.values.tolist()
#MyList2 is a list of 2 lists


class CalculatorForm(forms.Form):
    dep_city = forms.CharField(label='Departure Location:', widget=forms.Select(choices=MyList2)) # ? Check for default option in dropdowns
    des_city = forms.CharField(label='Destination location:', widget=forms.Select(choices=MyList2))
