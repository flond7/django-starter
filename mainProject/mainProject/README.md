- Ricordarsi di aprire l'intera cartella django su VS
- HDEAD: master

# INSTALL DJANGO FROM CDM 
- cd into c: (just tpe c:)
- cd C:\Users\PESSAE\Documents\webserver\django
- always create the **virtual environment** first and then the new django project (easier than conficuring a venv after project creation):
  python -m venv name-virtual-environment
- activate venv:
  C:\Users\PESSAE\Documents\webserver\django>name-virtual-environment\Scripts\activate
## make sure pip has the proxy
pip install --proxy=http://proxy-bc-el.regione.fvg.it:801 django
- create the project:
  django-admin startproject projectName  //creates the project folder (es mainProject)

# run server from cdm (inside project folder)
python mange.py runserver

# create database for user
- cd into ProjectName
- python manage.py migrate

# create superuser
python manage.py createsuperuser
(administrator - administrator@localhost.com - muni05cipio
http://127.0.0.1:8000/admin/

# CREATE A NEW APP
- cd into mainProject (aka mainProject parent folder)
- python manage.py startapp app-name
- add app-name to INSTALLED APPS in mainProject/mainProject/settings.py
  INSTALLED_APPS = [
    'django.contrib.admin',
    . . .
    'app-name',
  ]
- add urls to urlpatterns in mainProject/mainProject/urls.py use include in the form of path('api/', include('api.urls'))

# CREATE AN API
- requires, model, serializer, view and a migration
- *** IF NOT USING SQLite3 CREATE THE DATABASE HERE, BEFORE MAKING MIGRATIONS ***
- crete a model (table structure) in mainProject/api/models.py
- make a migration (to create the table) with: python manage.py makemigrations api
  (it creates a mainProject/api/migrations/0001_initial.py file and eventually a mainProject/db.sqlite3 if not present)
  to peak at the db see the section below
  *** REMEMBER THAT WHEN YOU NEED TO UPDATE A MIGRATION (A DB) THE COMMMAND IS: python manage.py migrate ***
  it creates a table that has app-name_model-name (es: api_women)
- create a serializer (transform tables data in python dictionaries - objects) in mainProject/api/serializer.py
- create a view in mainProject/api/viwes.py
  remember to import the model and the serializer in the view
- create an url path in mainProject/api/urls.py

python manage.py makemigrations

## DB PEAKING (SQLITE3)
- if it gives a CommandError: You appear not to have the 'sqlite3' program installed or on your path. copy the sql.exe file in the same folder as manage.py

- cd into mainProject and in a shell type command: python manage.py dbshell
- >>> table (to see all tables)
- >>> .schema --indent table-name (see the stricture)
- >>> select * from table-name
https://realpython.com/django-migrations-a-primer/

## DB MONGODB
- Install djnongo using: 
  pip install --proxy=http://proxy-bc-el.regione.fvg.it:801 djongo
- install the right mongoengine
  pip install --proxy=http://proxy-bc-el.regione.fvg.it:801 mongoengine
- install the right pymongo versione (eventually remove if its >4.0)
  pip install --proxy=http://proxy-bc-el.regione.fvg.it:801 pymongo==3.12.1 
- makemigrations and then migrate to change to mongoDB:
  python manage.py makemigrations
  python manage.py migrate  

*** WITH ERROR NotImplementedError: Database objects do not implement truth value testing or bool(). Please compare with None instead: database is not None ***
- pymongo version might be wrong, use 3.12.1
  pip uninstall pymongo
  pip install --proxy=http://proxy-bc-el.regione.fvg.it:801 pymongo==3.12.1 



## MANAGE URLS
- In main project folder urls.py you can link the ursl.py of a specific app within the main project inside urlpatterns in the form:
  path('sample/', include('sample.urls'))
- remember to have include imported at the top:
  from django.urls import path, include
- Create a ursl.py within the app folder to specify urls for the subfolder (the urs will be ip/root-name-main-urls/root-name-app-urls) :
  from django.urls import path
  from . import views
  urlpatterns = [
    path('pageOne', views.pageOneFunction, name='pageOneName'),
  ]
- In settings.py in the main projects add the string with the app name to INSTALLED APPS
  INSTALLED_APPS = [
    'django.contrib.admin',
    . . .
    'sample',
  ]



### CREATE VIEWS
- In the app folder views.py specify the functions that link to the template in the form

def pageOneFunction(request):
    return render(request, 'pageOne.html', {})

- In the app folder create a folder named templates and inside the pageOne.html. It's important to create templates because django will look for it

    sample/templates/pageOne.html



## GITHUB
git init 
git add README.md 
git config --global http.proxy http[s]://username:password@proxyipaddress:portnumber 
git config --global user.name "NICK" 
git config --global user.mail mail@gmail.com 
git config --global user.password ********* 
git commit -m "first commit" 
git branch -M main 
git remote add origin https://github.com/flond7/angular-startingPoint.git 
git push -u origin main

git branch (check branch name)
git branch -mv origin master (change name from origin to master)

git remote -v (check origin)
git remote set-url origin https://github.com/USERNAME/REPOSITORY.git (change repository)



## DJANGO REST FRAMEWORK
- in the api app add models (one table one model) modifying mainProject/api/models.py
- 





## REST
https://www.bezkoder.com/django-angular-crud-rest-framework/