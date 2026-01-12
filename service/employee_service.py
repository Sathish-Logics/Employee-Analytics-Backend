# SERVICE LAYER

from repository.employee_repo import (
    insert_employees,
    get_all_employees,
    get_employee_by_id,
    get_employee_by_name,
    get_employee_by_role,
    get_employee_by_department_id,
    get_employee_by_salary,
    update_name,
    update_role,
    update_department_id,
    update_salary
)

def create_employee(data):

    if not data.get("id"):
        raise ValueError("ID is required")

    if not data.get("name"):
        raise ValueError("Name is required")

    if len(data["name"]) > 30:
        raise ValueError("Name must be below 30 characters")

    if not data.get("role"):
        raise ValueError("Role is required")

    if data.get("salary", 0) < 15000:
        raise ValueError("Salary must be above 15000")

    insert_employees(
        data["id"],
        data["name"],
        data["role"],
        data["department_id"],
        data["salary"]
    )

def fetch_all_employees():
    return get_all_employees()

def fetch_employee_by_id(emp_id):

    if not emp_id:
        raise ValueError("Employee id required")

    employee = get_employee_by_id(emp_id)

    if not employee:
        raise ValueError("Employee not found")

    return employee

def fetch_employee_by_name(name):

    if not name:
        raise ValueError("Name is required")

    return get_employee_by_name(name)

def fetch_employee_by_role(role):

    if not role:
        raise ValueError("Role is required")

    return get_employee_by_role(role)

def fetch_employee_by_department_id(department_id):

    if not department_id:
        raise ValueError("Department id is required")

    return get_employee_by_department_id(department_id)

def fetch_employee_by_salary(salary):

    if salary is None:
        raise ValueError("Salary is required")

    if salary < 15000:
        raise ValueError("Salary must be above 15000")

    return get_employee_by_salary(salary)


def update_employee_name_service(data):

    if not data.get("id"):
        raise ValueError("ID required")

    if not data.get("name"):
        raise ValueError("Name cannot be empty")

    if len(data["name"]) > 30:
        raise ValueError("Name too long")

    update_name(data["id"], data["name"])

def update_employee_role_service(data):

    if not data.get("id"):
        raise ValueError("ID required")

    if not data.get("role"):
        raise ValueError("Role cannot be empty")

    update_role(data["id"], data["role"])

def update_employee_salary_service(data):

    if not data.get("id"):
        raise ValueError("ID required")

    if data.get("salary", 0) < 15000:
        raise ValueError("Salary must be above 15000")

    update_salary(data["id"], data["salary"])

def update_employee_department_service(data):

    if not data.get("id"):
        raise ValueError("Employee id is required")

    if not data.get("department_id"):
        raise ValueError("Department id is required")

    update_department_id(
        data["id"],
        data["department_id"]
    )
