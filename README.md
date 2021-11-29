# SSCM backend

## Constitution
Python 3.8.3   
Framework : Django 3.2.9

## Local:
### Installation
`$ pip install -r requirements/local.txt`  

### Migration:
`$ python manage.py migrate --settings=config.settings.local`

### Run application:
`$ python manage.py runserver --settings=config.settings.local`

## Production:

### Installation
`$ pip install -r requirements/production.txt`  

### Migration:
`$ python manage.py migrate --settings=config.settings.production`

### Run application:
`$ python manage.py runserver --settings=config.settings.production`

## Linters
#### Black: python code formatter:
`$ black directory/`

### Flake8
`$ flake8 --output-file=flake8.txt`  
configuration file is in setup.cfg