from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='dept_logos/', blank=True, null=True)

class Course(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='course_covers/', blank=True, null=True)

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='students/', blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='teachers/', blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
