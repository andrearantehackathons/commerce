# commerce

## Description

This is a website that allows users to either login and register with an account. Once they have an account, they can create their own auction listing and post it for other users to see. Using the "Active Listings" tab on the navbar, they can view all active listings and place their own bid. The owner of the listing has the ability to close auctions using the editing menu once a desirable bid has been recieved. Additionally, for user convenience it is possible to filter listing via the "filter by category" tab in the navbar. 

## Running/Setup Instructions

I think it is neccessary to make and apply migrations before running the project, so please run the following commands in the cmd before running

```
python manage.py makemigrations
python manage.py migrate
```

To start the server

```
python manage.py runserver
```
Then, navigate to this address in order to view the website. You will need to register in order to access full functionality of the website. 
http://127.0.0.1:8000/


