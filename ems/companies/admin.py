from django.contrib import admin
from .models import Company, Department
# Register your models here.
class CompanyAdmin(admin.ModelAdmin):

    readonly_fields = [
        'departments_count',
        'employees_count',
    ]


admin.site.register(Company, CompanyAdmin)
class DepartmentAdmin(admin.ModelAdmin):
    readonly_fields = [
        'employees_count',
    ]


admin.site.register(Department, DepartmentAdmin)
