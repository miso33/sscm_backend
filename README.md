# App backend

## Constitution
Python 3.8.3   
Framework : Django  3.2.8

## Local:

### Installation
Actualization: 17.10.2021  
`$ pip install -r requirements/local.txt`  

### Run application:
`python manage.py runserver --settings=config.settings.local`

### Best practies

#### Wrapper which verifies pep8, pyflakes and circular complexity
`$ flake8`

#### Python code formatter:
`$ black directory/`
 
## Production:

### Installation
`$ pip install -r requirements/production.txt`  
