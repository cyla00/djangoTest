# WINDOWS
## requirements:
* install => [PostgreSQL](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)<br/>
* install => [Anaconda or Miniconda](https://www.anaconda.com/products/individual)

## 1) setup of Anaconda virtual env for django
* to create a new virtual envyronment: ```$ conda create --name ENV_NAME```<br/>
* to activate the environment: ```$ conda activate ENV_NAME```<br/>
=>[useful docs for environment management](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands)<=<br/>

#### -now you are ready to install all the packages you need in the environment to run your projects

[install django](https://anaconda.org/anaconda/django):<br/>
```$ conda install -c anaconda django```<br/>
-to choose the django and/or python version to install:<br/>
```$ conda install -c anaconda django=VERSION_HERE python=VERSION_HERE```<br/>

[psycopg2](https://anaconda.org/anaconda/psycopg2):<br/>
```$ conda install -c anaconda psycopg2```<br/>

[install PostgreSQL](https://anaconda.org/anaconda/postgresql):<br/>
```$ conda install -c anaconda postgresql```<br/>

optional => [debug toolBar](https://anaconda.org/conda-forge/django-debug-toolbar):<br/>
```$ conda install -c conda-forge django-debug-toolbar```<br/>

## 2) creation of user and password for PostgreSQL
[create a role from the command line](https://www.postgresql.org/docs/8.1/sql-createrole.html) or from the PostgrteSQL UI then run ```$ createdb``` to create the base account database (named as username/rolename),
login from the command line using ```$ psql -U USERNAME```and enter password, from there you can run commands to show lists of users ```$ \du``` or ```$ \?``` for the commands list.

## 3) creation and connection of a django project
in the command line climb the path you want to put your project in and run ```$ django-admin startproject PROJECT_NAME```, a new folder named PROJECT_NAME and a ```./manage.py``` file are created.<br/>
Inside the folder there is a ```./settings.py``` file with a ```DATABASES``` variable, modify it depending on your [database type](https://docs.djangoproject.com/en/3.1/ref/settings/#databases);

### -run the script
to run the script climb to root path of your project folder where ```./manage.py``` is located and run ```$ python manage.py migrate```, after the migration run the server with ```$ python manage.py runserver```.
* check log => ```Starting development server at http://127.0.0.1:8000/``` (if running in local).

## 4) start writing the app
* The django file structure is basically a file "projects" that contains "apps", project urls.py is the one routing all the apps urls.py, and every app is responsible for a part of your site example: project=social network, apps=profile page/groups page/news page etc...<br/>
![file structure](https://djangobook.com/wp-content/uploads/structure_drawing1_new.png "base django project structure")

* create an app with: ```$ django manage.py startapp NAME_APP```<br/>
to add the app at the main project, go to root path ./settings.py and under INSTALLED_APPS, add as an app the folder name of the app just created.

## 5) app manipulation
the app itself is devided in 2 main parts, the view.py and urls.py, the view manages your html page (graphics) the url manages all the routes of the app.
example:
```py
#./view.py 
from django.shortcuts import render
from django.http import HttpResponse

def profile(request):
    return HttpResponse("render here your html file") #or
    return render('html file path')  
```

```py
#./url.py 
from django.urls import path, include
from . import views

urlpatterns = [
    path('url_path/', views.profile) #now he know that if the url contains "url_path/", he will render the "profile" function in views.py.
]
```

* the path of all the views will be: ```./templates/PROJECT_NAMED_FOLDER/html_files```, the templates folder should be created inside the application folder


is possible to extend and modulate the html files using:
```
{% block BLOCK_NAME %} 

html content 

{% endblock %}
```
extend to a main.html or base.html:<br/>
```
{% extends 'main.html file' %}

{% block BLOCK_NAME %} 

html content 

{% endblock %}
```
example add a pre-made header in main.html:<br/>
```
{% include 'path of main.html' %}
```