from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from employees.models import Employee
from employees.forms import EmployeeForm
from django.contrib.auth.models import User, Group


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

@login_required
def add_employee(request):

    user = request.user

    # Only admin and manager allowed
    if not (user.is_superuser or user.groups.filter(name='Manager').exists()):
        return redirect('home')

    if request.method == 'POST':
        form = EmployeeForm(request.POST)

        if form.is_valid():
            employee = form.save(commit=False)

            # Create username from email
            username = employee.email.split('@')[0]

            base_username = username
            counter = 1

            while User.objects.filter(username=username).exists():
                username = f"{base_username}{counter}"
                counter += 1


            # Create user account
            user = User.objects.create_user(
                username=username,
                email=employee.email,
                password='TempPass123'
            )

            # Assign Employee group
            employee_group = Group.objects.get(name='Employee')
            user.groups.add(employee_group)

            # Link employee to user
            employee.user = user
            employee.save()

            return redirect('home')

    else:
        # GET request → empty form
        form = EmployeeForm()


    return render(
        request,
        'employees/form.html',
        {
            'form': form,
            'title': 'Add Employee'
        }
    )