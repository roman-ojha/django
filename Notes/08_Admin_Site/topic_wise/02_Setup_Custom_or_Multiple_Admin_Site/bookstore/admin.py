from django.contrib import admin


class BookStoreAdminArea(admin.AdminSite):
    site_header = "Bookstore Admin Area"


bookstore_site = BookStoreAdminArea(name='BookstoreAdmin')

# and now register the model using this Admin
