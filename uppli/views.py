from django.http import HttpResponse
from django.shortcuts import render

from uppli.models import Employee


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def register_employee(request):
    if request.method == 'GET':
        employee = Employee.objects.all()
        return render(request,'register_employee.html',{'employee':employee})

    if request.method == 'POST':
        empid = request.POST.get('empid')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        role = request.POST.get('role')
        department = request.POST.get('department')
        hire_date = request.POST.get('hire_date')

    return render(request, 'register_employee.html')


# 出勤
def clock_in(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    today = timezone.now().date()
    attendance, created = Attendance.objects.get_or_create(employee=employee, date=today)

    if not attendance.clock_in_time:
        attendance.clock_in_time = timezone.now()
        attendance.save()
        message = "出勤時間を記録しました。"
    else:
        message = "すでに出勤時間が記録されています。"

    return render(request, 'attendance_message.html', {'message': message})

# 退勤
def clock_out(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    today = timezone.now().date()
    attendance = Attendance.objects.filter(employee=employee, date=today).first()

    if attendance and not attendance.clock_out_time:
        attendance.clock_out_time = timezone.now()
        attendance.save()
        message = "退勤時間を記録しました。"
    else:
        message = "出勤記録がないか、すでに退勤時間が記録されています。"

    return render(request, 'myapp/attendance_message.html', {'message': message})