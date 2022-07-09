from django.shortcuts import render
from .forms import CalculatorForm

# Create your views here.
# ? How to render a form in an already existing template
from django.http import HttpResponse, HttpResponseRedirect


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def calculator(request):
    return render(request, 'calculator.html')

def get_cities(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CalculatorForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/') # ! Redirect to a similar page with the result

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CalculatorForm()

    return render(request, 'calculator.html', {'form': form})