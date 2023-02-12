# Store_exam
A game store with a variety of products, consisting of an api in Django and Front End in React

## Quick install with Docker
1. Clone this repository on your device.

2. open a terminal and navigate to your repository directory

3. Run the command below in the terminal and wait the application building.

> docker-compose up -d --build

4. Okay, now you can use the application through the link http://localhost:3000/

## About the application

Using the installation with docker, 9 products and a user will already be created (User = UserTest and password = UserTest)

## Testing Backend

1. Include a file called localsetting.py in /setup/ resetting the settings requested below

~~~python
SECRET_KEY = 'SECRET KEY VALUE'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": 'django.db.backends.postgresql_psycopg2',
        "NAME": 'DATABASE NAME',
        "USER": 'DATABASE USER',
        "PASSWORD": 'DATABASE PASSWORD',
        "HOST": 'DATABASE HOST',
        "PORT": 'DATABASE PORT',
    }
}

~~~

2. Then create a virtual environment in your local directory and run it (the command varies depending on your operating system).

3. Use the command below to install the requirements

> pip install -r requirements.txt

4. Migrate the tables with the next command

> python manage.py migrate

5. Finally, run the tests with

> python manage.py test
