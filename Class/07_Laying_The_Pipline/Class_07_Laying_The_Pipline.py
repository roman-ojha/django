"""
urlpatterns = [
    # here we are building plipeline
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('removepunc',views.removepunc,name="rempun"),
    path('capitalizefirst',views.capfirst,name="capfirst"),
    path('newlineremove',views.newlineremove,name="newlineremove"),
    path('spaceremove',views.spaceremove,name="spaceremove"),
    path('charcount',views.charcount,name="charcount"),
]

in urls.py if we will write "DEBUG=false"
-> then it will show 404 error page if we will change other setting as well
"""