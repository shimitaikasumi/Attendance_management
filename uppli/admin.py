from django.contrib import admin

from uppli.models import Attendance, Employee


# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('empid', 'fname', 'lname', 'email', 'department', 'role', 'hire_date')
    search_fields = ('name', 'email', 'department', 'role')

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'clock_in_time', 'clock_out_time')
    list_filter = ('employee', 'date')
