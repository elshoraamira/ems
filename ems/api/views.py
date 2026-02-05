from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from employees.models import Employee
from companies.models import Company, Department
from .serializers import EmployeeSerializer, CompanySerializer, DepartmentSerializer
from .permissions import IsAdminOrManager

class CompanyViewSet(ModelViewSet):

    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [
        IsAuthenticated,
        IsAdminOrManager,
    ]

class DepartmentViewSet(ModelViewSet):

    serializer_class = DepartmentSerializer
    permission_classes = [
        IsAuthenticated,
        IsAdminOrManager,
    ]

    def get_queryset(self):

        user = self.request.user

        if user.is_superuser:
            return Department.objects.all()

        if user.groups.filter(name='Manager').exists():
            return Department.objects.filter(
                company=user.employee.company
            )

        return Department.objects.none()
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
