from django.shortcuts import render, HttpResponse

# Defining the function based Middleware


def my_middleware(get_response):
    # every middleware take 'get_response' as argument
    # One time initialized when server starts
    print("One time Initialization")

    def my_function(request):
        # bellow code will get executed before view get called
        print("This is before view")

        # now we will use 'get_response' function that pass to the next middleware or if this is the last middleware then it will pass to the view
        response = get_response(request)
        # and we will get response from view if this is the last middleware
        # or we will get response from the next middleware

        # now bellow code will get execute after view get called
        print("This is after view")

        # now we will return the response
        return response
    # and again we will return the function that we created inside middleware
    return my_function

# To activate this middleware you have to put this middleware into the 'MIDDLEWARE' on 'settings.py' file

# Defining the Class based Middleware


class MyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One time initialized when server starts
        print("One time Class Based Middleware Initialization")

    def __call__(self, request):
        # bellow code will get executed before view get called
        print("This is My before view")

        # now we will use 'get_response' function that pass to the next middleware or if this is the last middleware then it will pass to the view
        response = self.get_response(request)
        # and we will get response from view if this is the last middleware
        # or we will get response from the next middleware

        # now bellow code will get execute after view get called
        print("This is My after view")

        # now we will return the response
        return response

# To activate this middleware you have to put this middleware into the 'MIDDLEWARE' on 'settings.py' file


class BrotherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One time Brother Initialization")

    def __call__(self, request):
        print("This is Brother before view")
        response = self.get_response(request)
        print("This is Brother after view")
        return response


class FatherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One time Father Initialization")

    def __call__(self, request):
        print("This is Father before view")
        # so in this middleware if father did not get validated then we will not going to give access to the next middleware or a view
        # in that case we will response from here
        # response = HttpResponse("Invalid Father")
        # we can ever render the template from these middleware

        response = self.get_response(request)

        print("This is Father after view")
        return response


class MotherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One time Mother Initialization")

    def __call__(self, request):
        print("This is Mother before view")
        response = self.get_response(request)
        print("This is Mother after view")
        return response


class MyProcessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    # Middleware Hooks
    def process_view(request, *args, **kwargs):
        # this will get called before view
        # If this function will return None then it will call view
        # but if this function will return 'HttpResponse' then it will not going to call view and it will just response to the request client directly
        print("Process Middleware before view")
        # return HttpResponse("This is Before view")
        return None


class MyExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    # Middleware Hooks
    def process_exception(self, request, exception):
        # this function will get called whenever there will be and exception happen inside view
        # this will handle the exception
        # if this got the exception then we will response to client with some message
        msg = exception

        # get class name which throwing an exception
        class_name = exception.__class__.__name__
        print(class_name)

        return HttpResponse(msg)


class MyTemplateResponseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):
        print("Process template response from middleware")
        # getting context from the TemplateResponse
        # change the context value from here
        response.context_data['name'] = "Razz"
        # after manipulating the data we can return the response
        return response
