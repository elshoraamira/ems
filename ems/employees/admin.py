from django.contrib import admin
from .models import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)

        if request.user.is_superuser:
            return qs
        elif request.user.groups.filter(name='Manager').exists():
            return qs.filter(department=request.user.employee.department)
        else:
            return qs.filter(user=request.user)


admin.site.register(Employee, EmployeeAdmin)