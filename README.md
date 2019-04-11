# Menu Section API
## About
This is a simple menu section API created using Django REST Framework.
## Features
With this API you can do the following;
1)	Get a menu section by id
2)	Get all menu sections
3)	Add a new menu section
4)	Edit a menu section
5)	Delete a menu section
## Technology stack
Tools used during the development of this API are;
- [Django](https://www.djangoproject.com) - a python web framework
- [Django REST Framework](http://www.django-rest-framework.org) - a flexible toolkit to build web APIs
- [SQLite](https://www.sqlite.org/) - this is a database server
## Requirements
- Use Python 3.x.x+
## Test
```sh
    $ python manage.py test
```
## Instructions
1. Clone the repository to your local machine
    ```bash
        $ git clone https://github.com/tw2686/menu-rest-api.git
    ```
2. Install virtualenv
    ```bash
        $ pip install virtualenv
    ```
3. Go into the cloned repo:
    ```bash
        $ cd menu_api
    ```
4. Create and activate your virtual environment:
    ```bash
        $ virtualenv venv -p python3
        $ source venv/bin/activate
    ```
5. Install required dependencies:
    ```bash
        $ pip install -r requirements.txt
    ```
6. Make sure migrations work
    ```bash
        $ python manage.py makemigrations
        $ python manage.py migrate
    ```
7. Run the server
    ```bash
        $ python manage.py runserver
    ```
8. Go on browser and enter this link
    '''
      https://localhost:8000/menusection/
    '''
## How to Use
1)	Get a menu section by id
    """
      menusection/<id>
    """
    - refresh by clicking GET

2)	Get all menu sections
    """
      menusection/
    """
    - refresh by clicking GET

3)	Add a new menu section
    """
      menusection/
    """
    or
    """
      menusection/add
    """
    - input name and click POST

4)	Edit a menu section
    """
      menusection/<id>
    """
    or
    """
      menusection/<id>/edit
    """
    - input name and click PUT

5)	Delete a menu section
    """
      menusection/<id>
    """
    or
    """
      menusection/<id>/delete
    """
    - click DELETE
