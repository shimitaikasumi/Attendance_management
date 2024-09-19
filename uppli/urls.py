from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('register/', views.register_employee, name='register_employee'),
    path('clock_in/<int:employee_id>/', views.clock_in, name='clock_in'),
    path('clock_out/<int:employee_id>/', views.clock_out, name='clock_out'),
]