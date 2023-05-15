from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView


# Creating a new RedirectView using 'RedirectView'
class NewRedirectView(RedirectView):
    url = 'https://www.youtube.com'

    # pattern_name = ''


class SecondNewRedirectView(RedirectView):
    pattern_name = 'mainpk'

    # permanent = False(default) : gives 302 status code
    # permanent = True : gives 301 status code
    permanent = True

    query_string = True
    # query string is accepted on this url now and will not get remove on requesting using this url
    # default: False

    def get_redirect_url(self, *args, **kwargs):
        print(kwargs)
        # we ca access the dynamic url value and manipulate here as well
        kwargs['pk'] = 10
        return super().get_redirect_url(*args, **kwargs)
