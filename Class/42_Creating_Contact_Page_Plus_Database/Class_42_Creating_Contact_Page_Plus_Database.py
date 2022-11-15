"""
    => now here we will design contact page after that we will also write some backand for contact page in views.py

    => now we will create a model for the form that user fill and send the us from contact page 
            => class Contact(models.Model):
                product_id = models.AutoField(primary_key=True)
                name = models.CharField(max_length=50)
                email = models.CharField(max_length=70, default="")
                phone = models.CharField(max_length=70, default="")
                desc = models.CharField(max_length=500, default="")

                def __str__(self):
                    return self.product_name

            => after that we have to make migration to the new model so:
                -> python manage.py makemigrations
                -> python manage.py migrate
            
            => after that we will register the model in admin.py
                -> admin.site.register(Contact)
"""
