# Ecommerce-web-CRUD-API
A CRUD API for Products of an ECommerce shopping website.

HOW TO INSTALL AND RUN PROJECT LOCALLY -
1 - Create a Directory and create a virtualenv in it and activate it.
2 - clone the given code in this directory.
3 - open directory in a code editor(VS code or Pycharm).
4 - install requirements.txt file using command (pip install -r requirements.txt)
5 - run the mysql server locally and and also create a database named as 'products'
6 - run the command (python manage.py migrate)
7 - run another command (python manage.py createcachetable)
8 - There is a fixtures folder in which there is a JSON file.
9 - run (pathon manage.py loaddata) to load data in database
10 - run last command (python manage.py runserver)
11 - Now the api is accessible through the link - http://127.0.0.1:8000/productapi/

HOW TO USE IT - 
1 - If we send 'GET' request with the link given above, it responds with all data stored in MySql database and shows data in Json format. 
2 - For Creating a new data and storing it in the database, send the 'POST' request with the request body to the link given above.
3 - Request body has these fields - product_name, category, price, description, image, date. 
4 - To get the data of a particular product, we can make a 'GET' request by adding the ID of the product with the link. for example - http://127.0.0.1:8000/productapi/2/
5 - If we send 'PUT' or 'PATCH' requests with the request body through the link given above it will update the data of product id 2.
6 - we send 'PUT' requests for complete data fields update and 'PATCH' requests for partial data updates.
7 - For deleting a particular data, send a 'DELETE' request to the link with that particular product id. for example link given below deletes the product of id 3. Link - http://127.0.0.1:8000/productapi/3/
8 - I have added Database caching for 2 min cache timing. so if we send a GET request just after posting, updating, or deleting the data it will take some time (2 min) to show newly updated data.
