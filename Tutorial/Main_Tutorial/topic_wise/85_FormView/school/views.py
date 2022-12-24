from django.shortcuts import render
from .forms import ContactForm
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.http import HttpResponse


# using FormView class to render and validate form
class ContactFormView(FormView):
    # we will pass the form into the given template
    template_name = 'school/contact.html'
    # we will use the Form class to create a new form and it will automatically pass that form into the given template
    form_class = ContactForm

    # After successfully validate the form data when user submit we will redirect to the given url
    success_url = '/thankyou/'

    # passing the initial data when form is getting rendered
    initial = {'name': 'Roman', 'email': 'roman@gmail.com'}

    def form_valid(self, form):
        # we can get the form data after it get validate in this function
        form_data = form.cleaned_data
        print(form_data)

        # on this return it will redirect to 'success_url'
        return super().form_valid(form)

        # on this return it will ont redirect and response Http rather
        # return HttpResponse("Form submitted")

    def form_invalid(self, form):
        return super().form_invalid(form)


# redirect to this view after form got validate and get success
class ThanksTemplateView(TemplateView):
    template_name = 'school/thankyou.html'
