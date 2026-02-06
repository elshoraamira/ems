# Employee Management System (EMS)

A full-stack web application built with Django for managing companies, departments, and employees with role-based access control.

This system allows administrators, managers, and employees to manage and view data according to their roles.

---

## Features

### User Roles

#### Admin
- Manage companies, departments, and employees
- Assign managers
- View all system data

#### Manager
- View employees in own company and department
- Add and manage employees
- Read-only access to departments

#### Employee
- View personal profile only

---

### Core Functionality

- Company, Department, and Employee CRUD
- Automatic department & employee counting
- Employee status tracking
- Role-based permissions
- Dynamic department selection by company
- RESTful APIs
- Django Admin integration
- Session-based authentication

---

## Tech Stack

- Backend: Django, Django REST Framework
- Frontend: Django Templates, Bootstrap
- Database: SQLite (default)
- Authentication: Django Auth (Session-based)
- API: REST Framework

---

## Project Structure

```
ems/
├── api/
├── companies/
├── employees/
├── ems/
├── templates/
├── manage.py
├── requirements.txt
└── README.md
```

---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/elshoraamira/ems.git
cd ems
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Create Superuser

```bash
python manage.py createsuperuser
```

### 6. Run Server

```bash
python manage.py runserver
```

Open in browser:

```
http://localhost:8000
```

---

## User Access

### Admin

Created using:

```bash
python manage.py createsuperuser
```

Has full system access.

### Employees

- Created through Admin/Manager UI
- User account is automatically generated
- Temporary password is assigned on creation "TempPass123"

---

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| /api/companies/ | GET, POST | Manage companies |
| /api/departments/ | GET, POST | Manage departments |
| /api/employees/ | GET, POST | Manage employees |
| /api/departments/company/<id>/ | GET | Get departments by company |

---

## Business Rules

- Each employee is linked to one user account
- Managers are employees with special permissions
- Departments belong to one company
- Employees belong to one department
- Counts are auto-updated using Django signals
- Invalid company/department relations are blocked

---

## Validation & Security

- Email and phone validation
- Status-based hire date validation
- Role-based view permissions
- Protected delete operations
- Server-side and client-side validation

---

## Screenshots

```
screenshots/
├── admin_panel1.png
└── admin_panel2.png
```