from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, CompanyViewSet, DepartmentViewSet

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet, basename='employee')
router.register(r'companies', CompanyViewSet, basename='company')
router.register(r'departments', DepartmentViewSet, basename='department')

urlpatterns = router.urls