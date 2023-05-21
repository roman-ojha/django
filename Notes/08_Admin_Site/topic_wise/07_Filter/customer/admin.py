from .models import Profile, Order
from django.contrib.admin import SimpleListFilter
from django.contrib import admin
from django.db.models import *
# importing the third party admin filter package for Date range filter
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
from django.db.models.fields import FloatField, IntegerField
import datetime

# Blog: https://www.dothedev.com/blog/django-admin-list_filter/


# Creating the Custom filter:
# This filter is being used in django admin panel in profile model.
class BusinessEmailFilter(SimpleListFilter):
    # title/name of the filter that get displayed in Django admin filter sidebar
    title = 'Email Types'
    # so here we are selecting "User" model of "email" fields
    parameter_name = 'user__email'  # '<model>__<field>'

    def lookups(self, request, model_admin):
        # So here we will define what are the choices or options that we can use to filter
        return (
            # So here we are categorizing our email with 'business' & 'non-business' email
            # ('<django_use_as_value>','<human_readable_shown_in_admin>')
            ('business', 'Business'),
            ('non_business', 'Non Business')
        )

    # So here we created the REGEX so that we can filter using this, here we are validating about if the email is from 'hotmail', 'gmail', 'yahoo' then it is a non-business email
    SOCIAL_EMAIL_REGEX = r"^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(?!hotmail|gmail|yahoo)(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$"

    def queryset(self, request, queryset):
        # So filter is just the query so now we will build our one query which will then filter the record
        if not self.value():  # if we haven't select any options then return all the queryset
            return queryset
        if self.value().lower() == 'business':
            # now here we are filtering based on the business email
            return queryset.filter(user__email__regex=self.SOCIAL_EMAIL_REGEX)
        elif self.value().lower() == 'non_business':  # same goes not this filter
            return queryset.filter().exclude(user__email__regex=self.SOCIAL_EMAIL_REGEX)


# Range Filter:
# for that we will use the package 'django-admin-rangefilter'
# pip install django-admin-rangefilter

# Customizing range filter
# So if we want to filter a model which is not directly associated as a field but that model is been foreign key of the another model and we want to filter based on that
# EX: "Profile" model don't have direct link to "Order" model but the order does have connection with "Profile" model, and we want to filter those users who placed an order in given range in that case we will create the custom DateRangeFilter
class OrderPlacedFilter(DateRangeFilter):
    """
    This filter is being used in django admin panel in profile model.
    It filters out the customers who have placed orders in specified time limit.
    """
    parameter_name = 'placed_at'  # parameter name on the basis we want to filter

    def __init__(self, field, request, params, model, model_admin, field_path):
        # there will be use to populate the date fields inside admin filter
        self.lookup_kwarg_gte = '{}__gte'.format(self.parameter_name)
        self.lookup_kwarg_lte = '{}__lte'.format(self.parameter_name)
        # we are using the 'placed_at' filed from "Order" to filter
        field = Order._meta.get_field('placed_at')
        super(DateRangeFilter, self).__init__(field, request, params, Order, admin.site._registry[Order],
                                              "placed_at")
        self.request = request
        self.form = self.get_form(request)

    def queryset(self, request, queryset):
        # how here we will defining the queryset that how we will perform filter
        if not self.used_parameters:
            return queryset
        if self.form.is_valid():
            validated_data = dict(self.form.cleaned_data.items())
            if validated_data and (validated_data['placed_at__gte'] or validated_data['placed_at__lte']):
                order_placed_user = [order['user'] for order in Order.objects.filter(
                    **self._make_query_filter(request, validated_data)).distinct('user').values("user")]
                return queryset.filter(id__in=order_placed_user)
        return queryset

    def _make_query_filter(self, request, validated_data):
        """
        This method overrides the default kwargs generator for date_filter
        :param request:
        :param validated_data:
        :return:
        """
        query_params = {}
        date_value_gte = validated_data.get(self.lookup_kwarg_gte, None)
        date_value_lte = validated_data.get(self.lookup_kwarg_lte, None)

        if date_value_gte:
            query_params['{0}__gte'.format(self.field_path)] = self.make_dt_aware(
                datetime.datetime.combine(date_value_gte, datetime.time.min),
                self.get_timezone(request),
            )
        if date_value_lte:
            query_params['{0}__lte'.format(self.field_path)] = self.make_dt_aware(
                datetime.datetime.combine(date_value_lte, datetime.time.max),
                self.get_timezone(request),
            )

        return query_params


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "get_email", "full_name",
                    "created_at", "role", "is_verified")
    # By default when we will select some filters for the Date & time fields in that case django will search from greater then date to upto less then date
    # So, why don't we create the date picker from start date to the end date upto given date then it will going to filter the records
    # We are filtering with some fields
    list_filter = ("created_at", "role",
                   "is_verified")

    # Added "DateRangeFilter" on 'created_at' field
    # Added Custom "BusinessEmailFilter" filter
    list_filter = (("created_at", DateRangeFilter), ("created_at", DateTimeRangeFilter), "role",
                   "is_verified", BusinessEmailFilter)

    # Using "DateRangeFilter" you can now nest the mode with "<model>__<field>"
    list_filter = (("user__date_joined", DateRangeFilter), ("created_at", DateTimeRangeFilter), "role",
                   "is_verified", BusinessEmailFilter)

    # Using Custom DateRageFilter
    list_filter = (("created_at", OrderPlacedFilter), ("created_at", DateTimeRangeFilter), "role",
                   "is_verified", BusinessEmailFilter)


admin.site.register(Order)
