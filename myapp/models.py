from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.PositiveIntegerField()
    gender_choice=(
        ("male","male"),
        ("female","female")
    )
    gender=models.CharField(max_length=100,choices=gender_choice,default="male")
    department=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    address=models.TextField()

    def __str__(self):
        return self.name