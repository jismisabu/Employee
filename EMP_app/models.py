from django.db import models

class Employeemodel(models.Model):
    employee_name=models.CharField(max_length=100,null=False)
    employee_position=models.CharField(max_length=100,null=False)
    employee_place=models.CharField(max_length=100,null=True)
    employee_age=models.CharField(max_length=100)


    def __str__(self):
        return self.employee_name
