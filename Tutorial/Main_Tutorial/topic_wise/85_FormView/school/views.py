from django.shortcuts import render
from .forms import ContactForm
from django.views.generic.edit import FormView

# Create your views here.

# using FormView class to render and validate form


class ContactFormView(FormView):
    # we will pass the form into the given template
    template_name = 'school/contact.html'
    # we will use the Form class to create a new form and it will automatically pass that form into the given template
    form_class = ContactForm

    # After successfully validate the form data when user submit we will redirect to the given url
    success_url = '/thankyou/'
