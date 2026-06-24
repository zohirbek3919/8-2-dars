from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
    
class Bino(models.Model):
    name = models.CharField(max_length=255)
    qavat = models.PositiveIntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(25)],
        null=True, blank=True)
    manzil = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name