from django.contrib import admin
from .models import Student, Subject, Result

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'roll_number', 'email', 'created_at']
    search_fields = ['name', 'roll_number']

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']
    search_fields = ['name', 'code']

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['student', 'subject', 'marks_obtained', 'total_marks', 'grade', 'semester']
    search_fields = ['student__name', 'subject__name']
    list_filter = ['grade', 'semester']