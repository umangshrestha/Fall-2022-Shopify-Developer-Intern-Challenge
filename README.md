# Fall 2022 Shopify Challenge 
This repo is part of pre-interview for `Backend Intern` postion. The instructinos can be found here [instructions.pdf](doc/Fall2022-ShopifyDeveloperInternChallenge.pdf)

## 1. Tasks

<input type="checkbox" disabled checked /> CRUD Functionality  

<input type="checkbox" disabled /> When deleting, allow deletion comments and undeletion  

<input type="checkbox" disabled  checked/> Ability to create warehouses/locations and assign inventory to specific location

<input type="checkbox" disabled /> Ability to create “shipments” and assign inventory to the shipment, and adjust inventory
appropriately

## 2. Requirements
- Python3.9 
```
$ sudo apt update
$ sudo apt install software-properties-common
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt install python3.9
```
- Dependencies
```
$ pip install -u upgrade pip
$ pip install -r requirements.txt
```

## 3. Run the Script
```
$ python3 manage.py runserver 0.0.0.0:8000
```
## 3. Links
Since the task didnt ask for frontend, and I donot have any extra time I decided to use [Django](https://docs.djangoproject.com/en/4.0/) rest_framework's [browsable API](https://www.django-rest-framework.org/topics/browsable-api/) for basic UI interface. No GUI has been added for any of the operations.

To add the links:
1. List of Items --> [http://127.0.0.1:8000/items](http://127.0.0.1:8000/items/)
2. List of Warehouse --> [http://127.0.0.1:8000/warehouse](http://127.0.0.1:8000/warehouse)
3. Add new Items --> [http://127.0.0.1:8000/add/items](http://127.0.0.1:8000/items)
4. Add new Warehouse --> [http://127.0.0.1:8000/add/warehouse](http://127.0.0.1:8000/add/warehouse)
5. Edit prexisting Items --> [http://127.0.0.1:8000/items/\<id\>](http://127.0.0.1:8000/items/\<id\>)
6. Edit prexisting Warehouse --> [http://127.0.0.1:8000/warehouse/\<id\>](http://127.0.0.1:8000/warehouse/\<id\>)


here: `<id>` is an unique identifier integer for given object.

