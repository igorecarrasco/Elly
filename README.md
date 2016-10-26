# DJANGO

This is a testing platform for webapp tool Elly, my final project for studio 20.

### Sample .env file

Create .env file in root directory with the following key/values. Ask Igor for details.

	dbport=5432
	db=DBHERE
	dbuser=abc
	dbpassword=pass
	dbhost=hosturl
	saltkey=djangosalt
	parselytoken=parsleytokenhere
	parselyapikey=apikeyhere


## Run Locally

### requirements

 - install python, pip, virtualenv

### Turn on Virtualenv

	cd /DJANGO
	source venv/bin/activate

This source command turns on virtual environment to encapsulate python libraries.


### Install python requirements

	sudo pip install -r requirements.txt

### if you need to update python requirements

	# install the library
	pip install something

	# freeze to requirements
	pip freeze > requirements.txt


## Getting Django DB set up

	cd /studio3project 
	python manage.py migrate

## Run python ellyscraper

	cd ../ellyscraper/
	python ellyscraper.py

Once scraper is finished, data will be loaded into database

## Run Django 

	cd ../studio3project
	python manage.py runserver 

Visit <http://localhost:8000/elly>


### Turn off venv (optional)

	deactivate
