# Profiles REST API

REST API providing basic functionality for managing user Profiles

Installation commands to get started:

# pip install django==1.11
# pip install djangorestframework==3.6.2
# cd src/
# django-admin.py startproject restapi_profile_project
# This creates the restapi_profile_project in src/
# Dir lists:

04/11/2019  11:17 PM               843 manage.py
04/11/2019  11:17 PM    <DIR>          restapi_profile_project

# python manage.py startapp restapi_profile_app

This creates the restapi_profile_app folder

04/11/2019  11:17 PM               843 manage.py
04/12/2019  12:00 AM    <DIR>          restapi_profile_app
04/11/2019  11:59 PM    <DIR>          restapi_profile_project

Directory of C:\pythonProjects\workspace\python-rest-api\src\restapi_profile_project

Root level dir is - python-rest-API

We need to enable this restapi_profile_project settings in the django settings file.

Location: C:\pythonProjects\workspace\python-rest-api\src\restapi_profile_project\restapi_profile_project\settings.py

In this file, under INSTALLED_APPS: We need to add other installed apps - 'rest_framework',
  'rest_framework.authtoken', 'restapi_profile_app'

- You use the requirements.txt to specify the python packages with a specific version needed for this app;
- This way you can carry it to any other OS or image and install the same versions of the Py dependencies

- pip freeze # Lists the current packages and versions used in the virenv we are working on for a given project.

###

(env) C:\pythonProjects\workspace\python-rest-api\src\restapi_profile_project>pip freeze
Django==1.11
djangorestframework==3.6.2
pytz==2019.1

###  

cd to the project base dir:

pip freeze > requirements.txt

This creates the requirements.txt file at the root level.

###

Directory of C:\pythonProjects\workspace\python-rest-api

04/12/2019  12:13 AM    <DIR>          .
04/12/2019  12:13 AM    <DIR>          ..
04/11/2019  10:53 PM             1,819 .gitignore
04/11/2019  10:56 PM    <DIR>          env
04/12/2019  12:12 AM             1,707 README.md
04/12/2019  12:13 AM                56 requirements.txt
04/11/2019  11:17 PM    <DIR>          src
04/11/2019  10:52 PM             1,640 Vagrantfile

###

- We use Django development server to test the app; This is a basic web server provided by Django;

- run server is what you start for the development server;

- python manage.py runserver 0.0.0.0:8080 // Run server, make accessible on All IP on the server on Port 8080;

***
(env) C:\pythonProjects\workspace\python-rest-api\src\restapi_profile_project>python manage.py runserver 0.0.0.0:8080
Performing system checks...

System check identified no issues (0 silenced).

You have 15 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, authtoken, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
April 12, 2019 - 00:23:26
Django version 1.11, using settings 'restapi_profile_project.settings'
Starting development server at http://0.0.0.0:8080/
Quit the server with CTRL-BREAK.

***

Access using web browser : http://127.0.0.1:8080/   :-)

# DATABASE:

- After you create a custom model for a DB, you specify the project to use this custom model in the settings.py file
- Ex: AUTH_USER_MODEL = 'restapi_profile_app.UserProfile'

- You use the python manage.py makemigrations command to check our models, check the DB, and sync the DB;
- This will create and setup our DB for the first time.

- Under the app, you'll see a migrations folder with a new initial DB setup like - 0001_initial.py
**

(env) C:\pythonProjects\workspace\python-rest-api\src\restapi_profile_project>py manage.py makemigrations
Migrations for 'restapi_profile_app':
  restapi_profile_app\migrations\0001_initial.py
    - Create model UserProfile

**

- Then use the python manage.py migrate command; Will go through all our DB migrations and run on our DB;
- This will create the sqldblite file under the app.

# DjangoAdmin:

- Feature that gives us a whole administrative website that we can use to manage the models that we create in our DB;

- py manage.py createsuperuser
  Asks for username, password n so on..

  - You resgiter the models using DjangoAdmin

  - Go to admin.py file to register the models - admin.site.register(models.UserProfile)

- Test the DjangoAdmin by starting - python manage.py runserver 0.0.0.0:8080

- Then go to http://127.0.0.1:8080/admin/ 



# VAGRANT

- vagrant up
- vagrant ssh
- workon <project_name>
