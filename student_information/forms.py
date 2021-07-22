from django import forms
from student_information import models

class StudentForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = "__all__"