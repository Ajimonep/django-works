from django import forms
from myapp.models import Student

class StudentForm(forms.Form):

    name=forms.CharField()
    age=forms.IntegerField()
    gender=forms.ChoiceField(choices=Student.gender_choice)
    department=forms.CharField()
    phone=forms.CharField()
    email=forms.CharField()
    address=forms.CharField()