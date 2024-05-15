

from django.shortcuts import render
from .models import Student
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

class StudentDetailView(DetailView):
    model = Student
    template_name = 'app/student_detail.html'  # You need to specify a template name for DetailView

class StudentListView(ListView):
    model = Student
    template_name = 'app/student_list.html'  # You need to specify a template name for ListView
