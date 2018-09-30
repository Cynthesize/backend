# Django RESTful API + JWT authentication Boilerplate

A [Django](https://www.djangoproject.com/) REST API boilerplate.
this project uses: 
 - **[Django REST framework](http://www.django-rest-framework.org/)** for API.
 - **[JWT](https://jwt.io/)** for authentication process.

## Table of content

- [Django version](#django-version)
- [Getting started (Windows)](#getting-started-windows)
- [Deploy (Docker)](#deploy-docker)
- [License](#license)

## Django version

This project will focus on Django 2.0.7.

## Getting started (Windows):

1. **Install [Python 3.6](https://www.python.org/)**.
2. **Clone this repository** or [download the zip](https://github.com/Kamasado/Django-REST-API-JWT-boilerplate/archive/master.zip)
    ```bash
    git clone https://github.com/Kamasado/Django-REST-API-JWT-boilerplate
    ```
3. **Make sure you're in the directory you just created:**
    ```bash
    cd django-api-boilerplate
    ```
4. **Create a Python venv:**
    ```bash
    virtualenv .venv
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
    set DEV=true
    set DJANGO_SECRET=<YOUR_PROJECT_SECRET>
    ```
9. **Migrate models to database and Collect static files:**
    ```bash
    python manage.py makemigrations restapi
    python manage.py migrate
    python manage.py collectstatic
    ```
10. **Run development server:**
    ```bash
    python manage.py runserver 127.0.0.1:8001
    ```

## Deploy (Docker):

Required environment variables:
```bash
POSTGRESQL_ADDON_DB='<server db name>'
POSTGRESQL_ADDON_HOST='<DB_URL>'
POSTGRESQL_ADDON_PASSWORD=''
POSTGRESQL_ADDON_PORT=''
POSTGRESQL_ADDON_USER=''
DEV='false'
DJANGO_SECRET='<YOUR_DJANGO_SECRET>'
```
See [Dockerfile](Dockerfile) for details.

## License

This project follows the GNU GPLv3. See the [LICENSE](LICENSE) for details.
