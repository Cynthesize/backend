# Cynthesize

### Django Backend

[![Join the chat at https://gitter.im/oppia/oppia-chat](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/Cynthesize-gitter/Lobby)

## Setting up PostgreSQL
- **[Windows](https://doc.odoo.com/7.0/install/windows/postgres/)**: 
- **[Linux(Ubuntu)](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04)**: 
- **[MacOSx](https://www.codementor.io/engineerapart/getting-started-with-postgresql-on-mac-osx-are8jcopb)**: 

## Django version

This project will focus on Django 2.0.7.

## Getting started (Windows):

1. **Install [Python 3.6](https://www.python.org/)**.
2. **Clone this repository** or [download the zip](https://github.com/https://github.com/Cynthesize/backend/archive/master.zip)
    ```bash
    git clone https://github.com/Cynthesize/backend/
    ```
3. **Make sure you're in the directory you just created:**
    ```bash
    cd backend
    ```
4. **Create a Python venv:**
    ```bash
    virtualenv .venv
    ```
5. **Activate the venv:**
    ```bash
    "source .venv/bin/activate"
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
    export POSTGRESQL_ADDON_DB='<DB_NAME>'
    export POSTGRESQL_ADDON_HOST='<DB_HOST>'
    export POSTGRESQL_ADDON_PASSWORD='<DB_PASSWORD>'
    export POSTGRESQL_ADDON_PORT='<DB_PORT>'
    export POSTGRESQL_ADDON_USER='<DB_USER>'
    export DJANGO_SECRET='<YOUR_DJANGO_SECRET>'
    ```
9. **Migrate models to database and Collect static files:**
    ```bash
    python manage.py makemigrations users
    python manage.py makemigrations ideas
    python manage.py migrate users
    python manage.py migrate ideas
    python manage.py collectstatic
    ```
10. **Run development server:**
    ```bash
    python manage.py runserver <PORT_NUMBER>
    ```

## Deploy (Docker):

Required environment variables:
```bash
  POSTGRESQL_ADDON_DB='<DB_NAME>'
  POSTGRESQL_ADDON_HOST='<DB_HOST>'
  POSTGRESQL_ADDON_PASSWORD='<DB_PASSWORD>'
  POSTGRESQL_ADDON_PORT='<DB_PORT>'
  POSTGRESQL_ADDON_USER='<DB_USER>'
  DJANGO_SECRET='<YOUR_DJANGO_SECRET>'
```
See [Dockerfile](Dockerfile) for details.

## License

This project follows the GNU GPLv3. See the [LICENSE](LICENSE) for details.
