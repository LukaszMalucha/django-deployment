## DJANGO DEPLOYMENT

### Heroku

cd myapp

git init

git add .

git commit -m "My first commit"

git push heroku master

<br>

heroku domains:add www.example.com

heroku domains:wait 'www.example.com'

<br>

openssl genrsa -des3 -out server.pass.key 2048

openssl rsa -in server.pass.key -out server.key


### Digital Ocean

##### SSH

Putty -> ssh

adduser <name>

usermod -aG sudo <name>  (give sudo privilages)

su <name>

sudo apt-get update

sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx  (paste with right-click)

#### Postgres

sudo -u postgres psql

CREATE USER db_admin WITH PASSWORD '<password>'

ALTER ROLE db_admin SET client_encoding TO 'utf8';

ALTER ROLE db_admin SET default_transaction_isolation TO 'read committed';

ALTER ROLE db_admin SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE droplet TO db_admin;

\q

#### Create a Python Virtual Environment 

sudo -H pip3 install --upgrade pip

sudo -H pip3 install virtualenv

cd /home

mkdir droplet

cd droplet/

virtualenv env

source env/bin/activate

#### Configure Django Project

pip install django gunicorn psycopg2

#### Upload Project with Filezilla

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

sudo chmod -R 777 /home/lukasz/droplet/src/staticfiles/

python manage.py collectstatic

sudo chmod -R 740 /home/lukasz/droplet/src/staticfiles/


#### Allow Port 8000

gunicorn --bind 0.0.0.0:8000 droplet.wsgi

#### Gunicorn System Service file

deactivate

##

[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=sammy
Group=www-data
WorkingDirectory=/home/sammy/myproject
ExecStart=/home/sammy/myproject/myprojectenv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/sammy/myproject/myproject.sock myproject.wsgi:application

[Install]
WantedBy=multi-user.target

##

sudo systemctl start gunicorn

sudo systemctl enable gunicorn

cd ..

sudo chgrp -R www-data src

sudo chmod -R g+w src/

cd src

sudo systemctl daemon-reload
sudo systemctl restart gunicorn


#### Nginx
sudo nano /etc/nginx/sites-available/droplet

##

server {
    listen 80;
    server_name server_domain_or_IP;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/sammy/myproject;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/sammy/myproject/myproject.sock;
    }
}

##

sudo ln -s /etc/nginx/sites-available/droplet /etc/nginx/sites-enabled

sudo nginx -t

sudo systemctl restart nginx

sudo ufw delete allow 8000

sudo ufw allow 'Nginx Full'


