## Description

Document Archiving system is made for archive simple document.

## Installation

Installing the latest stable version is simple. But make sure first you have python install on your system.
You can use virtualenv or any wrapper for create Virtual Environment. I have used **pipenv

   `$ pip install pipenv`
   
[Check this for more information about pipenv](https://docs.pipenv.org/en/latest/)

## Install directly from git.
    $ git clone https://github.com/purkayasta/Document-Archiving-catalog.git
    $ cd Document-Archiving-catalog
    $ pipenv install
    
## Make sure delete all the migrations in the migration folder and do database migration.
    $ python manage.py makemigrations
    $ python manage.py migrate
    
## Run the app by writting this commad.
    $ python manage.py runserver

## Heroku Deployment (*Coming*)


# Some screenshot are given below

## Homepage
![homepage](https://user-images.githubusercontent.com/12936435/64678206-f27f6c80-d49a-11e9-8f91-7b7ad1f06647.png)


## 2.Upload
![upload](https://user-images.githubusercontent.com/12936435/64678224-fa3f1100-d49a-11e9-9ef4-8ec5698478c1.png)

## 3.Searching
![searching](https://user-images.githubusercontent.com/12936435/64678217-f6ab8a00-d49a-11e9-92fd-59201746b906.png)

