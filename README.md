# Microsoft-Outlook-OAuth-system
This project implements an Microsoft Outlook OAuth system that enables users to both login and sign up while ensuring the continuous management of user sessions and authentication tokens.

## Requirements 
$ python3.10.x

## Running server manually 

$ Replace All configuration with microsoft credentials in oauth_setting.yaml file

$ pip3 install -r requirements.txt

$ python3 manage.py makemigrations

$ python3 manage.py migrate

$ python3 manage.py runserver

## Running server through docker

$ docker build -t ms-auth .

$ docker run -p 8000:8000 ms-auth

## API endpoints
$ / : Home page, requires signin if not signed in automatically redirects to outlook signin

$ v1/signin : If signed in redirects to home page else automatically redirects to outlook signin

$ v1/signout : Clears the user session

$ v1/callback : Auth user response from Authorisation server

## DB schema

$ User model : (id : int, user_name: str, email: str)


## Flow diagram

![flow diagram]('https://raw.githubusercontent.com/vishal-s-patil/Microsoft-Outlook-OAuth-system/main/ms-Auth.png')
