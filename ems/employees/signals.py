from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Employee
@receiver(post_save, sender=Employee)
@receiver(post_delete, sender=Employee)
def update_employee_counts(sender, instance, **kwargs):
    company = instance.company
    department = instance.department

    company.employees_count = company.employees.count()
    company.save(update_fields=['employees_count'])

    department.employees_count = department.employees.count()
    department.save(update_fields=['employees_count'])