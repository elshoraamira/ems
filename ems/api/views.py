from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from employees.models import Employee
from .serializers import EmployeeSerializer


class EmployeeListView(ListAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        # Superuser: see all
        if user.is_superuser:
            return Employee.objects.all()

        # Manager: see own department
        if user.groups.filter(name='Manager').exists():
            return Employee.objects.filter(
                department=user.employee.department
            )

        # Employee: see self only
        return Employee.objects.filter(user=user)