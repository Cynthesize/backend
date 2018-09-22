# Django RESTful API + JWT authentication 

A [Django](https://www.djangoproject.com/) REST API
this project uses: 
 - **[Django REST framework](http://www.django-rest-framework.org/)** for API.
 - **[JWT](https://jwt.io/)** for authentication process.


## Django version

This project will focus on Django 2.0.7.

## Getting started (Windows):

1. **Install [Python 3.6](https://www.python.org/)**.
2. **Clone this repository**
    ```bash
    git clone https://github.com/WickedBrat/backend
    ```
3. **Make sure you're in the directory you just created:**
    ```bash
    cd backend
    ```
4. **Create a Python venv:**
    ```bash
    virtualenv -p python3 .venv
    ```
5. **Activate the venv:**
    ```bash
    ".venv/Scripts/activate"
    ```
6. **Install Python requirements:**
    ```bash
    pip install -r requirements.txt
    ```
7. **Move to source directory:**
    ```bash
    cd src/
    ```
8. **Set required environment variables:**
    ```bash
    export DEV=true
    export DJANGO_SECRET=<YOUR_PROJECT_SECRET>
    ```
9. **Migrate models to database and Collect static files:**
    ```bash
    python manage.py makemigrations restAPI
    python manage.py migrate
    python manage.py collectstatic
    ```
10. **Run development server:**
    ```bash
    python manage.py runserver 127.0.0.1:8001
    ```
