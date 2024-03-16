from django.db import models

# Create your models here.


class Student_data(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    department=models.CharField(max_length=100,default='CSE')
    class Meta:
        db_table = "Student_data"

    def __str__(self):
        return self.email


class Faculty_profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    class Meta:
        db_table = "Faculty_Profile"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class HOD_profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    #username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = "HOD_Profile"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
class Files(models.Model):
    file_name = models.CharField(max_length=100)
    class Meta:
        db_table = "Files"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



# class UploadedFiles(models.Model):
#     file1 = models.FileField(upload_to='uploads/')
#     file2 = models.FileField(upload_to='uploads/')
#     uploaded_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"UploadedFiles {self.id}"

class StudentFacultyMapping(models.Model):
    student_registration_number = models.CharField(max_length=20)
    student_name = models.CharField(max_length=100)
    student_branch = models.CharField(max_length=50)
    student_email = models.EmailField()
    faculty_name = models.CharField(max_length=100)
    faculty_email = models.EmailField()
    faculty_phone = models.CharField(max_length=20)


    def __str__(self):
        return f"{self.student_name} - {self.faculty_name}"

from django.contrib.auth.models import User
from django.db import models

class MyUploadedFiles(models.Model):
    roll_number = models.PositiveIntegerField()  # Add a Roll No field
    weekly_report = models.FileField(upload_to='uploads/')
    certificate = models.FileField(upload_to='uploads/')
    ppt = models.FileField(upload_to='uploads/')
    final_project_report = models.FileField(upload_to='uploads/')
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=20)
    marks1 = models.PositiveIntegerField(default=0)
    marks2 = models.PositiveIntegerField(default=0)
    marks3 = models.PositiveIntegerField(default=0)
    marks4 = models.PositiveIntegerField(default=0)
    marks5 = models.PositiveIntegerField(default=0)
    marks6 = models.PositiveIntegerField(default=0)
    marks7 = models.PositiveIntegerField(default=0)
    marks8 = models.PositiveIntegerField(default=0)
    average_marks = models.FloatField(default=0.0)


    def __str__(self):
        return f"{self.roll_number}"


class PrivateFile(models.Model):
    file = models.FileField(upload_to='private_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    student_mapping = models.ForeignKey(StudentFacultyMapping, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student_mapping}"


class Company(models.Model):
    internship_dates = models.DateField()
    company_name = models.CharField(max_length=255)
    job_location = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    eligibility_criteria = models.TextField()
    stipend = models.DecimalField(max_digits=10, decimal_places=2)
    application_url = models.URLField()

    def __str__(self):
        return self.company_name


class Document(models.Model):
    DOMAIN_CHOICES = [
        ('Web Development', 'Web Development'),
        ('AIML', 'AIML'),
        ('DATA SCIENCE', 'DATA SCIENCE'),
    ]

    title = models.CharField(max_length=255)
    domain = models.CharField(max_length=20, choices=DOMAIN_CHOICES)
    # file = models.FileField(upload_to='documents/')
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


from django.utils import timezone
from datetime import timedelta
class Circular(models.Model):
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

    @classmethod
    def delete_old_records(cls):
        # Calculate the date 3 weeks ago
        three_weeks_ago = timezone.now() - timedelta(weeks=3)
        # Delete records older than 3 weeks
        cls.objects.filter(created_at__lt=three_weeks_ago).delete()

class UploadedFiles(models.Model):
    file1 = models.FileField(upload_to='uploads/%Y/%m/%d/')
    file2 = models.FileField(upload_to='uploads/%Y/%m/%d/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Uploaded Files - {self.uploaded_at}"