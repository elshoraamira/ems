from django.db import models

# Create your models here.
class Department(models.Model):
    company = models.ForeignKey('companies.Company', on_delete=models.CASCADE, related_name='departments')
    name = models.CharField(max_length=255)
    employees_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        # Return department name along with company name for better identification of the department (since we have many companies)
        return f"{self.name} - {self.company.name}"