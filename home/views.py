"""
Views of MVC
"""
from django.shortcuts import render
from django.http import HttpResponseRedirect
import pandas as pd
from .models import Calculator
from .forms import CalculatorForm

# Create your views here.


CITY_LIST = pd.read_excel("./home/static/home/data_files/worldcities.xlsx")

MyList = CITY_LIST[['city', 'city_ascii', 'lat', 'lng']]
LatLon = CITY_LIST[['lat', 'lng']]

MyList2 = MyList.values.tolist()
MyList3 = MyList.to_dict('records')

def get_cities(request):
    """
    This function renders the calculator page
    """
    submitbutton = request.POST.get('Calculate')

    dep_city = ''
    des_city = ''

    form = CalculatorForm(request.POST or None)
    if form.is_valid():
        dep_city = form.cleaned_data.get('dep_city')
        des_city = form.cleaned_data.get('des_city')

    context={'form':form,'dep_city': dep_city, 'des_city': des_city}

    return render(request, 'calculator.html', context)

def result(request):
    """
    Result display"""
    dep_city = ''
    des_city = ''

    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid:
            dep_city = request.POST["dep_city"]
            des_city = request.POST["des_city"]

            des_latitude = 0
            des_longitude = 0

            dep_latitude = 0
            dep_longitude = 0

            for i in MyList3:
                if i['city'] == des_city:
                    des_latitude = i['lat']
                    des_longitude = i['lng']    

                loc1 = (des_latitude, des_longitude)

                if i['city'] == dep_city:
                    dep_latitude = i['lat']
                    dep_longitude = i['lng']              

                loc2 = (dep_latitude, dep_longitude)

                Mydistance = Calculator.calculateDistance(loc1, loc2)

                MyCarbon = Calculator.calculateCarbon(Mydistance)

                Killings = Calculator.killings(MyCarbon) # A tuple

                Leopard = Killings[0]
                Lion = Killings[1]
                Buffalo = Killings[2]
                Rhino = Killings[3]
                Elephant = Killings[4]


            context={'form':form,'dep_city': dep_city, 'des_city': des_city, 'Mydistance': Mydistance, 'MyCarbon': MyCarbon, 'Leopard' : Leopard, 'Lion' : Lion, 'Buffalo' : Buffalo, 'Rhino' : Rhino, 'Elephant' : Elephant}

            return render(request, 'result.html', context)
    else:
        form = CalculatorForm()
        return HttpResponseRedirect('')
