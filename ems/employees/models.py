from datetime import date
from django.core.exceptions import ValidationError
from django.db import models
from companies.models import Company, Department
from django.contrib.auth.models import User
import re
# Create your models here.
class Employee(models.Model):
    STATUS_CHOICES = [
        ('application', 'Application Received'),
        ('interview', 'Interview Scheduled'),
        ('hired', 'Hired'),
        ('rejected', 'Not Accepted'),
    ]

    company = models.ForeignKey(Company, on_delete=models.PROTECT, related_name='employees')
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name='employees')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=22, unique=True)
    address = models.TextField()
    designation = models.CharField(max_length=255)
    hired_on = models.DateField(null=True, blank=True) # Can be null if not hired yet
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def clean(self):
        if self.department and self.company:
            if self.department.company_id != self.company_id:
                raise ValidationError(
                    "Selected department does not belong to the selected company."
                )
        
        if self.status == 'hired' and not self.hired_on:
            raise ValidationError(
                "Hired date must be provided when employee status is 'Hired'."
            )
        
        # Non-hired must NOT have date
        if self.status != 'hired' and self.hired_on:
            raise ValidationError(
                "Hired date can only be set when status is 'Hired'."
            )
    
        if not re.fullmatch(r'\d{10,15}', self.mobile):
            raise ValidationError(
                "Mobile number must contain 10–15 digits only."
            )
    
    @property
    def days_employed(self):
        if self.status == 'hired' and self.hired_on:
            return (date.today() - self.hired_on).days
        return None
    
    def __str__(self):
        return f"{self.name} ({self.company.name})"