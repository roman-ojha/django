"""
-> in views.py change all the GET request to POST
-> when you are using POST request there is a CSRF varification 
-> CFRS Token Cross Site Request Forgery)
    -> it is the token that provide security to your website
    -> and it is the promise where the request is comming from you own website
    -> https://docs.djangoproject.com/en/3.2/ref/csrf/
    -> In the template, there is a {% csrf_token %} template tag inside each POST form that targets an internal URL 

    -> just go to the index.html and inside the form tag write {% csrf_token %}
"""