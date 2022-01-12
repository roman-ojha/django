"""
=> Now we will need to introduce template in our project for that we will
    -> in setting.py we can see 'BASE_DIR' which will gives us the base directory of the project

-> now we will going to create a template folder inside the base directory
    -> and now we will going to add :
        -> 'DIRS': [
            os.path.join(BASE_DIR, "templates")
        ],
        -> in setting.py "TEMPLATES"

-> and we will going to create folder 'template/tweets' which will content all the template related to 'tweets' application and 'template/pages'
    -> now we will render the template from views.py:
            -> return render(request, 'pages/home.html', context={}, status=200) 
"""
