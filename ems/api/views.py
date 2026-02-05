from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from employees.models import Employee
from .serializers import EmployeeSerializer
from .permissions import IsAdminOrManager


class EmployeeViewSet(ModelViewSet):

    serializer_class = EmployeeSerializer
    permission_classes = [
        IsAuthenticated,
        IsAdminOrManager,
    ]

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            return Employee.objects.all()

        if user.groups.filter(name='Manager').exists():
            return Employee.objects.filter(
                department=user.employee.department
            )

        return Employee.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
