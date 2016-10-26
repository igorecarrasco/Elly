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

### Turn off venv

	deactivate


### Install python requirements

	sudo pip install -r requirements.txt

### update python requirements

	# install the library
	pip install something

	# freeze to requirements
	pip freeze > requirements.txt