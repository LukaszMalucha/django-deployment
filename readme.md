### DJANGO DEPLOYMENT

#### Heroku

cd myapp\
git init\
git add .\
git commit -m "My first commit"\
git push heroku master

heroku domains:add www.example.com
heroku domains:wait 'www.example.com'

openssl genrsa -des3 -out server.pass.key 2048
openssl rsa -in server.pass.key -out server.key