from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Course(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(100)],
        null=True, blank=True)
    hudud = models.CharField(max_length=255)
    category = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name