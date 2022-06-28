# Ecommerce-web-CRUD-API
A CRUD API for Products of an ECommerce shopping website.

HOW TO USE IT -
1 - Create a Directory and create a virtualenv and activate it.
2 - clone the given code.
3 - open this directory in a code editor.
4 - install requirements.txt file using command (pip install -r requirements.txt)
5 - run the mysql server locally and and also create a database named as 'products'
6 - run the command (python manage.py migrate)
7 - run another command (python manage.py createcachetable)
8 - there is a fixture folder in which a json file is putted.
9 - run (pathon manage.py loaddata) to load data in database
10 - run last command (python manage.py runserver)
11 - Now the api is accessible through the link - http://127.0.0.1:8000/productapi/
