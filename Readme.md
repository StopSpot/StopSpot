# Stop Spot
 
## Purpose
 
## Tech Stack
 
## Django Installation 
 
## Installing Leaflet and Tutorials 
 
To install the needed map packages for Stop Spot use the following command: 
```
pip install django-leaflet
```
If you're interested in using leaflet in your Django project, the following links are helpful:  
https://github.com/makinacorpus/django-leaflet 

https://django-leaflet.readthedocs.io/en/latest/index.html
 
## Setting up Initial migrations 
 
## Importing Data and setting up Postgresql 
First, you'll need to install Postgresql on your machine. We found that https://www.postgresql.org/download/ was easy to navigate and the installation was fairly straightforward. 
*We strongly recommend creating a password you only use for Postgres as it easy to push it to your repo*
 
Once installed, set up a database named SysMap in Postgres. Then head to the file settings.py in the ctran_project_env_1 folder and update the database section to include the password you created during installation. 
 
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'SysMap',
        'USER': 'postgres',
        'PASSWORD': 'password_goes_here',
        'HOST': 'localhost'
    }
}
```
Once all these steps are done, try running
```
python3 manage.py runserver
```
in the SysMap folder to see if the connection to Postgres is working. 

