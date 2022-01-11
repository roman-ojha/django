"""
-> now we can be able to see the model that we had made in database
-> we made the model in models.py file and we migrate it as will 
-> now to add Product we have to make a super user
-> and that user have power to do anything in db
-> to make superuser write in terminal:
    -> python manage.py createsuperuser
    -> now it will ask some question to configure fill the field
    -> Username: roman
    -> Email address: .env.EMAIL
    -> Password: 1234 (Not recomended and not secure)
-> now we create superuser
-> we know that in 'env/urls.py' we had :
        -> path('admin/', admin.site.urls),
-> now go the that url and login in by putting Username and Password
-> but after login we dont see the 'Product' table so, to see that 
-> if we make a table in 'models.py' we have to register the model in 'shop/admin.py'
-> now go and register in 'admin.py'
-> to register write in 'admin.py':
    -> admin.site.register(Product)

-> now in admin url we will see product
-> now you can add the product manully as well form the website
"""
