"""
-> while doing some project we in template most of the time in every page of the html we have to put the same content like:
    -> navigation
    -> fotter
    -> and some content we have to repate in our website
-> at that time we have to follow the dry principle and to make that possible we have template inheritance concept in django
-> so to do that we will make a about.html file in shop/templates/shop/about.html and basic.html in the same directory
-> firstly we will render the about.html in /about url so to do that we will write:
    -> def about(request):
    return render(request, 'shop/about.html')
    -> in views.py

-> now but we will design the about page by using the dry principle
-> so now we will write the basic template inside the basic.html
-> so now we will put {% extends shop/basic.html %}
-> it means that in about.html all the basic code will be copied or replecated
-> now in basic.html in title tage we will write:
    -><title>{% block title%} {% endblock %}</title>
    -> now in here we are trying to re use from the basic
    -> so we will put firstly in basic.html from that we will inherite to other page
    -> now inside that block what every we will write will inherite the whole basic page and put the spacific content on the page we are inheriting

-> so now to write the title in about we will put:
    -> {% block title%} {% endblock %}
    -> in about.html and inside it we will write the title of the about page like:
        -> {% block title%} about page {% endblock %}
        -> it means that throught that basic template now we can also change the content of page and make the same tempalte throught: {% %} {% %}

-> now after that we will also want to add style in our page which is inherited form the basic.html so we will write:
    -> <style>
      {% block css %} {% endblock %}
    </style>
    -> inside the basic.html so that inside that block while making website we can write as per our wish

-> and we know that insid the template we also want design our body so we have to write:
    -> {% block body %} {% endblock %}
    ->in side the body in basic.html where we want to edit in our exact wesite

-> now we will going to inherite the index.html as well by:
"""
