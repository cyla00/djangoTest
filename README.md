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
inside the folder there is a ```./settings.py``` file with a ```DATABASES``` variable, modify it depending on your [database type](https://docs.djangoproject.com/en/3.1/ref/settings/#databases);

### -run the script
to run the script climb to root path of your project folder where ```./manage.py``` is located and run ```$ python manage.py migrate```, after the migration run the server with ```$ python manage.py runserver```.
* check log ```Starting development server at http://127.0.0.1:8000/``` (if running in local).

