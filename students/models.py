from django.db import models


class Student(models.Model):

    student_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=20)
    civil_status = models.CharField(max_length=30, blank=True)
    nationality = models.CharField(max_length=50, default="Filipino")

    email = models.EmailField()
    contact_number = models.CharField(max_length=20)
    address = models.TextField()

    father_name = models.CharField(max_length=150, blank=True)
    mother_name = models.CharField(max_length=150, blank=True)
    guardian_name = models.CharField(max_length=150, blank=True)
    guardian_contact = models.CharField(max_length=20, blank=True)

    previous_school = models.CharField(max_length=200, blank=True)
    last_grade_completed = models.CharField(max_length=50, blank=True)
    strand = models.CharField(max_length=50, blank=True)

    course = models.CharField(max_length=100)
    year_level = models.CharField(max_length=30)
    section = models.CharField(max_length=50, blank=True)
    academic_year = models.CharField(max_length=20)
    student_type = models.CharField(max_length=20)
    enrollment_status = models.CharField(max_length=30, default="Enrolled")
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_id} - {self.first_name} {self.last_name}"
