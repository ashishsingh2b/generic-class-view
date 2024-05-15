from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import StudentData
from django.views.generic.list import ListView
# Create your views here.

class Student(ListView):
    model =StudentData
    template_name = 'app/student.html'
    context_object_name = 'std'

    def get_queryset(self):
        return StudentData.objects.filter(course='Django')
    
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context ['freshers']= StudentData.objects.all().order_by('name') 
        return context
    
    def get_template_names(self):
        if self.request.COOKIES ['user'] == 'Ashish':
            template_name = 'app/Ashish.html'
        else:
            template_name = self.template_name
        return [template_name]
