from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    is_manager = forms.BooleanField(
        required=False,
        label="Is Manager"
        )
    class Meta:
        model = Employee

        fields = [
            'company',
            'department',
            'name',
            'email',
            'mobile',
            'address',
            'designation',
            'status',
            'hired_on',
        ]
