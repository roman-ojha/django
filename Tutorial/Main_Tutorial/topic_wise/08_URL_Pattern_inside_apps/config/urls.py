from django.contrib import admin

from django.urls import path, include
from course import views as courseViews
from fees import views as feesViews


courseUrlPatterns = [
    # /course2/dj/
    path('dj/', courseViews.learn_django),
    # /course2/py/
    path('py/', courseViews.learn_python),
]

feesUrlPatterns = [
    # /fees2/dj/
    path('dj/', feesViews.fees_django),
    # /fees2/py/
    path('py/', feesViews.fees_python),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('course/', include('course.urls')),
    path('fees/', include('fees.urls')),

    # another way to create Urls for application folder views
    # for this method we don't have to create 'urls.py' file in every application folder
    # Course Application:
    path('course2/', include([
        # /course2/dj/
        path('dj/', courseViews.learn_django),
        # /course2/py/
        path('py/', courseViews.learn_python),
    ])),
    # Fees Application:
    path('fees2/', include([
        # /fees2/dj/
        path('dj/', feesViews.fees_django),
        # /fees2/py/
        path('py/', feesViews.fees_python),
    ])),

    # Another Way to Create URls for application folder views
    path('course3/', include(courseUrlPatterns)),
    # Fees Application:
    path('fees3/', include(feesUrlPatterns)),
]
