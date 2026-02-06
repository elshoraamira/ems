from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, CompanyViewSet, DepartmentViewSet, departments_by_company
from django.urls import path, include

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet, basename='employee')
router.register(r'companies', CompanyViewSet, basename='company')
router.register(r'departments', DepartmentViewSet, basename='department')

urlpatterns = [
    path('', include(router.urls)),
    path('departments/company/<int:company_id>/', departments_by_company),
]