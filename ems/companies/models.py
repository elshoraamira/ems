from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255)
    department_count = models.PositiveIntegerField(default=0)
    employees_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name