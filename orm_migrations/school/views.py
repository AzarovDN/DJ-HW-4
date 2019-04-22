from django.views.generic import ListView

from .models import Student


class StudentListView(ListView):
    model = Student
    ordering = 'group'

    def get_queryset(self):
        return Student.objects.all().prefetch_related('teacher')
