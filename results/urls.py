from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.add_student, name='add_student'),
    path('results/', views.result_list, name='result_list'),
    path('results/add/', views.add_result, name='add_result'),
]