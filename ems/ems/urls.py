"""
URL configuration for ems project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import employee_list, add_employee, edit_employee, delete_employee, company_list, add_company, edit_company, delete_company, add_department, edit_department, delete_department
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', employee_list, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('employees/add/', add_employee, name='add_employee'),
    path('employees/<int:pk>/edit/', edit_employee, name='edit_employee'),
    path('employees/<int:pk>/delete/', delete_employee, name='delete_employee'),
    path('companies/add/', add_company, name='add_company'),
    path('companies/<int:pk>/edit/', edit_company, name='edit_company'),
    path('companies/<int:pk>/delete/', delete_company, name='delete_company'),
    path('departments/add/', add_department, name='add_department'),
    path('departments/<int:pk>/edit/', edit_department, name='edit_department'),
    path('departments/<int:pk>/delete/', delete_department, name='delete_department'),
]