from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from employees.models import Employee


@login_required
def employee_list(request):

    user = request.user

    is_manager = user.groups.filter(name='Manager').exists()

    if user.is_superuser:
        employees = Employee.objects.all()

    elif is_manager:
        employees = Employee.objects.filter(
            department=user.employee.department
        )

    else:
        employees = Employee.objects.filter(user=user)

    return render(
        request,
        'employees/list.html',
        {
            'employees': employees,
            'is_manager': is_manager,
        }
    )