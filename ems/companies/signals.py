from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Company, Department

@receiver(post_save, sender=Department)
@receiver(post_delete, sender=Department)
def update_company_department_count(sender, instance, **kwargs):
    company = instance.company
    company.departments_count = company.departments.count()
    company.save(update_fields=['departments_count'])