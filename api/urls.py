from django.urls import path

from api import views
from api.views import EmployeeViewsetview, Employeelistcreate, Employeemixin

from rest_framework.routers import DefaultRouter


router=DefaultRouter()

router.register('v2/employee',views.EmployeeViewsetview,basename="employee")



urlpatterns=[
    path('employee/',Employeelistcreate.as_view(),name="emp"),
    path('employee/<int:pk>',Employeemixin.as_view(),name="mixin"),

]+router.urls