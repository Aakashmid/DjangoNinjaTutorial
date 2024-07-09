from ninja import NinjaAPI

from datetime import date
from ninja import Schema
from .models import Employee
api = NinjaAPI()

# input schema for Employee data ( means how receving data should be like)
class EmployeeIn(Schema):
    first_name: str
    last_name: str
    department_id: int = None
    birthdate: date = None

@api.post("/employees")
def create_employee(request, payload: EmployeeIn):
    employee = Employee.objects.create(**payload.dict())
    return {"id": employee.id}