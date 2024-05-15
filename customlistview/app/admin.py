from django.contrib import admin
from .models import StudentData
# Register your models here.

@admin.register(StudentData)
class StudentDetals(admin.ModelAdmin):
    list_display = ['id','name','roll','course']