from django.shortcuts import render
from .models import Student
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


# Create your views here.
class StudentDetailView(DetailView):
    # Providing the 'Student' model for this view
    model = Student
    # Because this return the object detail rather then List
    # it means that while running this view from the route it expect 'pk'

    # Default template name for this model 'student_detail.html'
    # Setting custom template name
    template_name = 'school/student.html'
    # Now default template name will now work

    # Default context for this model is 'student'
    # Setting custom context object name
    context_object_name = 'st'

    # to change the default 'pk' kwargs to query 'Student' Detail
    pk_url_kwarg = 'id'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        # passing all remaining student so that we can navigate to the specific student page from other specific student page
        context['remaining_student'] = self.model.objects.exclude(
            id=context['object'].id)
        return context


class StudentListView(ListView):
    model = Student
