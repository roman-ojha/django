from django.db import models

# Create your models here.


class Product(models.Model):
    """
    here we are making the class 'Product' and inherit from 'models.Model'
    """
    product_id = models.AutoField
    # here we are making the id of the product and that id is autogenerate
    # documentation: https://docs.djangoproject.com/en/3.2/ref/models/fields/
    product_name = models.CharField(max_length=50)
    # now here we are making the product_name and we know that product_name have the character so we have to use 'models.CharField(max_length = <maximum_length_of_producto_name>)
    desc = models.CharField(max_length=300)
    # discreption
    pub_date = models.DateField()
    # publised field
