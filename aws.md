### AWS

##### Python

pip install awscli

pip install awsebcli

aws configure --profile <Name>

AWS Access Key

AWS Secret

None 

None

##### AWS Deployment

Elastic Beanstalk - use N. Virginia (or other US) env for free deployment, otherwise will throw an error

Give Administrator Access Permission Group to the user

Give ElasticBeanstalk Permission Group to the user

Create C:\Users\<Username>/.aws/credentials if not have it

##### Python EBCLI

eb init

eb create (application)

Create .ebextensions/django.config

eb deploy

*** Deploy django.config on two stages: 1-option_settings, 2-container_commands to avoid errors

*** Make sure that requirements.txt are in correct folder

*** Make sure that wsgi.py and manage.py are pointing to correct settings file

##### POSTGRES

Create management-commands-makesuper

Add Configuration-Database-Edit-Postgres-dbAdmin-<password>
 

##### S3 STATIC HOSTING

Give user S3 Full Access permission