from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from employees.models import Employee
from employees.forms import EmployeeForm
from django.contrib.auth.models import User, Group

from companies.models import Company, Department
from companies.forms import CompanyForm, DepartmentForm

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

    # Companies (admin only)
    companies = None

    if user.is_superuser:
        companies = Company.objects.all()

    departments = None

    if user.is_superuser:
        departments = Department.objects.select_related('company')

    elif is_manager:
        departments = Department.objects.filter(
            company=user.employee.company
        ).select_related('company')
        
    return render(
        request,
        'employees/list.html',
        {
            'employees': employees,
            'is_manager': is_manager,
            'companies': companies,
            'departments': departments,
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
            is_manager = form.cleaned_data.get('is_manager')

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

            # Assign group
            employee_group = Group.objects.get(name='Employee')
            manager_group = Group.objects.get(name='Manager')

            user.groups.add(employee_group)

            if is_manager:
                user.groups.add(manager_group)

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

@login_required
def edit_employee(request, pk):

    employee = Employee.objects.get(pk=pk)
    user = request.user
    is_manager = user.groups.filter(name='Manager').exists()

    # Permission check
    if not (user.is_superuser or (is_manager and employee.department == user.employee.department) or employee.user == user):
        return redirect('home')

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)

        if form.is_valid():
            employee = form.save()

            is_manager = form.cleaned_data.get('is_manager')

            manager_group = Group.objects.get(name='Manager')

            if is_manager:
                employee.user.groups.add(manager_group)
            else:
                employee.user.groups.remove(manager_group)

            return redirect('home')

    else:
        user_is_manager = employee.user.groups.filter(name='Manager').exists()

        form = EmployeeForm(
            instance=employee,
            initial={'is_manager': user_is_manager}
        )

    return render(
        request,
        'employees/form.html',
        {
            'form': form,
            'title': 'Edit Employee'
        }
    )

@login_required
def delete_employee(request, pk):

    employee = Employee.objects.get(pk=pk)
    user = request.user
    is_manager = user.groups.filter(name='Manager').exists()

    if not (user.is_superuser or (is_manager and employee.department == user.employee.department)):
        return redirect('home')

    if request.method == 'POST':
        employee.user.delete()
        employee.delete()

        return redirect('home')

    return render(
        request,
        'employees/confirm_delete.html',
        {
            'object': employee,
            'type': 'Employee'
        }
    )

@login_required
def company_list(request):

    if not request.user.is_superuser:
        return redirect('home')

    companies = Company.objects.all()

    return render(
        request,
        'companies/list.html',
        {
            'companies': companies
        }
    )

@login_required
def add_company(request):

    if not request.user.is_superuser:
        return redirect('home')

    if request.method == 'POST':
        form = CompanyForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = CompanyForm()

    return render(
        request,
        'companies/form.html',
        {
            'form': form,
            'title': 'Add Company'
        }
    )

@login_required
def edit_company(request, pk):

    if not request.user.is_superuser:
        return redirect('home')

    company = Company.objects.get(pk=pk)

    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)

        if form.is_valid():
            form.save()
            return redirect('home')
        
    else:
        form = CompanyForm(instance=company)

    return render(
        request,
        'companies/form.html',
        {
            'form': form,
            'title': 'Edit Company'
        }
    )

@login_required
def delete_company(request, pk):

    if not request.user.is_superuser:
        return redirect('home')

    company = Company.objects.get(pk=pk)

    if request.method == 'POST':
        company.delete()
        return redirect('home')


    return render(
        request,
        'companies/confirm_delete.html',
        {
            'object': company,
            'type': 'Company'
        }
    )

@login_required
def add_department(request):

    if not request.user.is_superuser:
        return redirect('home')

    if request.method == 'POST':
        form = DepartmentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
        
    else:
        form = DepartmentForm()

    return render(
        request,
        'departments/form.html',
        {
            'form': form,
            'title': 'Add Department'
        }
    )

@login_required
def edit_department(request, pk):

    if not request.user.is_superuser:
        return redirect('home')

    department = Department.objects.get(pk=pk)

    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = DepartmentForm(instance=department)

    return render(
        request,
        'departments/form.html',
        {
            'form': form,
            'title': 'Edit Department'
        }
    )

@login_required
def delete_department(request, pk):

    if not request.user.is_superuser:
        return redirect('home')

    department = Department.objects.get(pk=pk)

    if request.method == 'POST':
        department.delete()
        return redirect('home')

    return render(
        request,
        'departments/confirm_delete.html',
        {
            'object': department,
            'type': 'Department'
        }
    )

