from django.db import models

# Create your models here.
class Course(models.Model):
    coursename=models.CharField(max_length=255,null=True)
    coursefee=models.IntegerField(null=True)

    def __str__(self):
        return self.coursename


class Student(models.Model):
    studentname=models.CharField(max_length=255,null=True)
    address=models.CharField(max_length=255,null=True)
    age=models.IntegerField(null=True)
    date=models.DateField(null=True)
    course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.studentname