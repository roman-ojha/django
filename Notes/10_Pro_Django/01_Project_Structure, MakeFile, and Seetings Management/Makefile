# We will going to need a lots of command like:
# python manage.py runserver
# python manage.py makemigrations
# python manage.py migrate
# and others
# so rather then write all of these command from the terminal we will going to create a makefile

# Creating the custom command
runserver: # Now we can run 'make runserver'
# poetry run python manage.py runserver
# beause we have moved the manage.py file into 'core' we have to run the module level file
	poetry run python -m core.manage runserver

.PHONY: install # by default these 'install', 'migrate' are called as target and makefile will assume that these are files but we want to epacify that these aren't a files rather these are custom commands, because of that it will increase performance because make won't have to search for any files
# and also it will exclude the conflict of running files or a command
install:
	poetry install
	
.PHONY: migrate 
migrate:
	poetry run python -m core.manage migrate

.PHONY: makemigrations 
makemigrations:
	poetry run python -m core.manage makemigrations
	
.PHONY: createsuperuser 
createsuperuser:
	poetry run python -m core.manage createsuperuser

.PHONY: update 
update: install migrate; # combining multiple make command that we wrote above and creating new command