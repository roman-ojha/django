"""
-> python -m pip install pipenv --upgrade
    -> to setup python virtual environment we have to first install 'pipenv'
    -> or: pip install pipenv
-> pipenv

-> here we are using python djanog=2.2
    -> pipenv install --python 3.10 django==2.2

    -> pipenv shell
        -> this will activate our virtual environment
        -> we will get:
            -> 'Pipfile'
            -> 'Pipfile.lock'
        -> this comes by default to every shell

-> now we can run :
    -> django-admin
        -> so we will create a project:
            -> django-admin startproject tweetme .
            -> '.' for the current directory

-> now in vsCode at the buttom left side we can see "Python <version>" click it and select the venv for this project

-> now in terminal it will open it as:
    -> (tweetme) PS <"project directory">

-> and we will install the recomended package for python env:
    -> -m pip install -U autopep8
"""
