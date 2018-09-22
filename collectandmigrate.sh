export POSTGRESQL_ADDON_DB=''
export POSTGRESQL_ADDON_HOST=''
export POSTGRESQL_ADDON_PASSWORD=''
export POSTGRESQL_ADDON_PORT=''
export POSTGRESQL_ADDON_USER=''
export DEV='false'
export DJANGO_SECRET=''

python ./manage.py collectstatic
python ./manage.py migrate
