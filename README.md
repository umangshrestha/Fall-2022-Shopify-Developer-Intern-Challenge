# Fall 2022 Shopify Challenge 
This repo is part of pre-interview for `Backend Intern` postion. The instructinos can be found here [instructions.pdf](doc/Fall2022-ShopifyDeveloperInternChallenge.pdf)

## 1. Tasks

[x] disabled checked /> CRUD Functionality  

[ ] When deleting, allow deletion comments and undeletion  

[x] Ability to create warehouses/locations and assign inventory to specific location

[ ] Ability to create “shipments” and assign inventory to the shipment, and adjust inventory
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
$ pip install --upgrade pip
$ pip install -r requirements.txt
```

## 3. Run the Script
```
$ python3 manage.py runserver 0.0.0.0:8000
```
## 4. Links
Since the task didn't ask for frontend, and I donot have any extra time I decided to use [Django](https://docs.djangoproject.com/en/4.0/) rest_framework's [Browsable API](https://www.django-rest-framework.org/topics/browsable-api/) for basic UI interface. No GUI has been added for any of the operations.

To add the links:
- List of Items --> [http://127.0.0.1:8000/items](http://127.0.0.1:8000/items/)
- List of Warehouse --> [http://127.0.0.1:8000/warehouse](http://127.0.0.1:8000/warehouse)
- Add new Items --> [http://127.0.0.1:8000/add/items](http://127.0.0.1:8000/items)
- Add new Warehouse --> [http://127.0.0.1:8000/add/warehouse](http://127.0.0.1:8000/add/warehouse)
- Edit prexisting Items --> [http://127.0.0.1:8000/items/\<int: id\>](http://127.0.0.1:8000/items/\<id\>)
-  Edit prexisting Warehouse --> [http://127.0.0.1:8000/warehouse/\<int: id\>](http://127.0.0.1:8000/warehouse/\<id\>)

here: `<int:id>` is an unique identifier integer for given object.

