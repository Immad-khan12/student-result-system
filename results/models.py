from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.roll_number})"

class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Result(models.Model):
    GRADE_CHOICES = [
        ('A+', 'A+'), ('A', 'A'), ('B+', 'B+'),
        ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F'),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks_obtained = models.IntegerField()
    total_marks = models.IntegerField(default=100)
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES)
    semester = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.student.name} - {self.subject.name} - {self.grade}"