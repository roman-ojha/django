from django.shortcuts import render
from django.views.generic.base import TemplateView

#


# Creating 'TemplateView' class and overriding some of the method and property that we want
class HomeTemplateView(TemplateView):
    template_name = 'school/home.html'

    # Passing context data into template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Setting new value into context
        context['name'] = "Roman"
        context['roll'] = 25

        # OR:
        # context = {'name': 'Roman', 'roll': 25}
        # but this will override the context and the super value that it contain

        # kwargs contain data like dynamic url data etc..
        print(kwargs)
        # and these value will get provided to template as context as well

        return context
