from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.IntegerField()
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(max_length=15)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    last_education = models.CharField(max_length=100)

    def __str__(self):
        return self.name
