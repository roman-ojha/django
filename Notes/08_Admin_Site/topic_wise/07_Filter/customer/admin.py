from .models import Profile
from django.contrib.admin import SimpleListFilter
from django.contrib import admin
from .models import *


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


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "get_email", "full_name",
                    "created_at", "role", "is_verified")
    # We are filtering with some fields
    # Added Custom "BusinessEmailFilter" filter
    list_filter = ("created_at", "role", "is_verified", BusinessEmailFilter)

    # By default when we will select some filters for the Date & time fields in that case django will search from greater then date to upto less then date
    # So, why don't we create the date picker from start date to the end date upto given date then it will going to filter the records


admin.site.register(Order)
