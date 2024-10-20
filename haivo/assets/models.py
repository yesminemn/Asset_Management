from django.db import models

# Create your models here.
class Asset(models.Model):
    name = models.CharField(max_length=100)
    available = models.BooleanField(default=True)  # Tracks availability of the asset

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Lending(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
