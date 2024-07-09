from django.contrib import admin
from .models import Employee,Department
# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','department','birthdate']

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display=['id','title']
