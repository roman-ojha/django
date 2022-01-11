from django.db import models
from django.db.models.fields.files import ImageField

# Create your models here.


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    # making a category of the product
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    # making price of the product
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name
