from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255)
    departments_count = models.PositiveIntegerField(default=0)
    employees_count = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name

class Department(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT, related_name='departments')
    name = models.CharField(max_length=255)
    employees_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        # Return department name along with company name for better identification of the department (since we have many companies)
        return f"{self.name} - {self.company.name}"