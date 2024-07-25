from django.shortcuts import get_object_or_404
from ninja import NinjaAPI, UploadedFile, File
from .schemas import EmployeeIn, EmployeeOut, DepartmentIn, DepartmentOut
from .models import Employee, Department
from typing import List

api = NinjaAPI()

@api.get("/test")
def test(request):
    return {'test': 'success'}

@api.post("/department")
def create_department(request, payload: DepartmentIn):
    department = Department.objects.create(**payload.dict())
    return {"id": department.id}

@api.get("/departments", response=List[DepartmentOut])
def list_departments(request):
    qs = Department.objects.all()
    return qs

@api.post("/employees")
def create_employee(request, payload: EmployeeIn):
    employee = Employee.objects.create(**payload.dict())
    return {"id": employee.id}

@api.get("/employees/{employee_id}", response=EmployeeOut)
def get_employee(request, employee_id:int):
    employee = get_object_or_404(Employee, id=employee_id)
    return employee

@api.get("/employees", response=List[EmployeeOut])
def list_employees(request):
    qs = Employee.objects.all()
    return qs

@api.put("/employees/{employee_id}")
def update_employee(request, employee_id: int, payload: EmployeeIn):
    employee = get_object_or_404(Employee, id=employee_id)
    for attr, value in payload.dict().items():
        setattr(employee, attr, value)
    employee.save()
    return {"success": True}

@api.delete("/employees/{employee_id}")
def delete_employee(request, employee_id: int):
    employee = get_object_or_404(Employee, id=employee_id)
    employee.delete()
    return {"success": True}