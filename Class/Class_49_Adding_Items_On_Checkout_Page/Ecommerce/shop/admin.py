from django.contrib import admin

# Register your models here.
from .models import Contact, Product
# here we know we had made the table name 'Product'
# so we are importing it

admin.site.register(Product)
admin.site.register(Contact)
