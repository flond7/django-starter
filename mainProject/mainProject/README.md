- Ricordarsi di aprire l'intera cartella django su VS
- HDEAD: master

# installa django in windows from cdm
## cd into c
c:
cd C:\Users\PESSAE\Documents\webserver\django
## create virtual environment
python -m venv name-virtual-environment
## activate venv
C:\Users\PESSAE\Documents\webserver\django>name-virtual-environment\Scripts\activate
## make sure pip has the proxy
pip install --proxy=http://proxy-bc-el.regione.fvg.it:801 django

django-admin startproject projectName  //creates the project folder 

# run server from cdm (inside project folder)
python mange.py runserver

# create database for user
- cd into ProjectName
- python manage.py migrate

# create superuser
python manage.py createsuperuser
(administrator - administrator@localhost.com - muni05cipio
http://127.0.0.1:8000/admin/

# create new app
python manage.py startapp app-name




### URL
- In main project folder urls.py you can link the ursl.py of a specific app within the main project inside urlpatterns in the form

    path('sample/', include('sample.urls'))

- remember to have include imported at the top

    from django.urls import path, include

- Create a ursl.py within the app folder to specify urls for the subfolder (the urs will be ip/root-name-main-urls/root-name-app-urls) 

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







## REST
https://www.bezkoder.com/django-angular-crud-rest-framework/