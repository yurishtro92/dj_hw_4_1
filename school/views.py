from django.views.generic import ListView
from django.shortcuts import render
from .models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'
    students = Student.objects.order_by('group')
    teachers = Teacher.objects.all()
    context = {
        'students': students,
        'teachers': teachers
    }
    return render(request, template, context)



