from django.shortcuts import render

# Create your views here.


def home(request):
    # NOTE: the context that we pass from here that can be able to access from 'core/home.html' but if that template include another template then that template can also access the context passed from here
    return render(request, 'core/home.html', {'about_url': '/about', 'top_course_template': ['Dart', 'Vue', 'React', 'Typescript']})


def about(request):
    return render(request, 'core/about.html', {'home_url': '/'})
