from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Subject, Result

def home(request):
    total_students = Student.objects.count()
    total_subjects = Subject.objects.count()
    total_results = Result.objects.count()
    return render(request, 'results/home.html', {
        'total_students': total_students,
        'total_subjects': total_subjects,
        'total_results': total_results,
    })

def student_list(request):
    students = Student.objects.all()
    return render(request, 'results/student_list.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        roll_number = request.POST['roll_number']
        email = request.POST['email']
        Student.objects.create(name=name, roll_number=roll_number, email=email)
        return redirect('student_list')
    return render(request, 'results/add_student.html')

def result_list(request):
    results = Result.objects.all()
    return render(request, 'results/result_list.html', {'results': results})

def add_result(request):
    if request.method == 'POST':
        student = get_object_or_404(Student, id=request.POST['student'])
        subject = get_object_or_404(Subject, id=request.POST['subject'])
        marks = request.POST['marks_obtained']
        total = request.POST['total_marks']
        grade = request.POST['grade']
        semester = request.POST['semester']
        Result.objects.create(
            student=student, subject=subject,
            marks_obtained=marks, total_marks=total,
            grade=grade, semester=semester
        )
        return redirect('result_list')
    students = Student.objects.all()
    subjects = Subject.objects.all()
    return render(request, 'results/add_result.html', {
        'students': students,
        'subjects': subjects,
    })