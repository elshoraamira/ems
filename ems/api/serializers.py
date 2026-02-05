from rest_framework import serializers
from employees.models import Employee
from companies.models import Company, Department

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            'id',
            'name',
            'departments_count',
            'employees_count',
        ]

        read_only_fields = [
            'departments_count',
            'employees_count',
        ]
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = [
            'id',
            'name',
            'company',
            'employees_count',
        ]

        read_only_fields = [
            'employees_count',
        ]
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            'id',
            'name',
            'email',
            'mobile',
            'designation',
            'status',
            'department',
            'company',
            'hired_on',
        ]