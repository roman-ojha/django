from django.urls import path, register_converter
from . import views, converters

# now we will register the converter that we created
register_converter(converters.FourDigitYearConverter, 'yyyy')
# register_converter(<converter_class>,'<path_converter_name>')

urlpatterns = [
    # now accessing the path converter that we created
    path('session/<yyyy:year>/', views.show_details, name='detail'),
]
