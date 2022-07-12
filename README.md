<center> <h1>Sustravels </h1></center>


## ALX SE Program Final Portfolio Project

Sustravels is a website that allows travelers to check how much damage their travel is doing to the environment. 
It will be implemented as a web application with an embedded carbon calculator that enables the user to gauge their carbon emissions as well as how many animals they will be killing. 
It will also offer alternatives to offset these emissions through eco-tourisms resorts and hotels, airlines that offset emissions and other recommendations.



---


## Installation

Make sure you have python3 installed with venv. If you don't have [venv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/), you can install it with:

```bash
python3 -m pip install --user virtualenv
```

Clone the repository:

```bash
git clone https://github.com/Virgo-Alpha/Sustravels.git
```

Cd on the root folder of the project

Make a .env file and make any random set of characters your secret key. The .env file can contain (as an example):
```bash
SECRET_KEY=123
```


Create the virtual environment with
```bash
make create_environment
```

Then, you can activate it with:
```bash
source env/bin/activate
```

And install dependencies with:
```bash
make install
```
With all dependencies installed, you can check other quick make commands from the Makefile.

Install the django environ module using the following command:
```bash
 pip install django-environ
```

Apply migrations using the following command:
```bash
 python manage.py migrate
```


To run the django server, use the command:
```bash
python manage.py runserver
```

You can the go to your browser and type:
```
http://127.0.0.1:8000/calculator/
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Initiating a django Project
Install django using instructions from here: [django installation](https://docs.djangoproject.com/en/4.0/topics/install/#installing-official-release/)

After installation, follow this [tutorial](https://docs.djangoproject.com/en/4.0/intro/tutorial01/) to make your project.

