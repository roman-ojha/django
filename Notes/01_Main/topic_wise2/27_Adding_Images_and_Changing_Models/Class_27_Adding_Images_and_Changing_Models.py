"""
-> in this tutorial we are adding some of the model again:
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField(upload_to="shop/images")

-> now we know we had change the model now we have to migrate it
    -> python manage.py makemigrations
    -> after that it will show :
        -> Please select a fix:
                1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
                2) Quit, and let me add a default in models.py
                Select an option:
    -> it is saying that we had already made the model and have some data in the database and we are again changing the model
    -> and we now also have to imagefiled but in previous data don't have imagefield because of that it is asking us
    -> now just quite it by entering 2
    -> and add 'default=""' in some filed
    -> subcategory = models.CharField(max_length=50, default="")
        image = models.ImageField(upload_to="shop/images", default="")
        price = models.IntegerField(default=0)
    -> here we are adding these field to previouse data and making default value for that
    -> now again write:
        ->  python manage.py makemigrations
    -> now migrations will happen
    -> now in this case we will see '0002_auto_20210818_1057.py' file in migraions folder
    -> it means it store the changes that we had did in the model
    -> now to migrate or to store the changes in the database write:
        -> python manage.py migrate
    

-> we can see in the /admin/ url website in product table , we have 'Product object(2), Product object(1)'
-> but we want some name
-> to do that we will define method in 'models.py' file inside 'Product' class
    -> def __str__(self):
        return self.product_name

-> now in admin website in shop/product if we will add another product and add the image to that product then we can see that automatically inside the shop app folder there will create a folder name 'image' inside that we will see the uploaded image

-> but this is not the recomended way to upload any media file
-> so in next tutorial we will see how we will define 'media' directory hwo we will define media url and we can push all the media inside that media
"""
