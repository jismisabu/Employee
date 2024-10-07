from django import forms
from EMP_app.models import Employeemodel


class Employeeform(forms.Form):
    employee_name=forms.CharField(max_length=100)
    employee_position=forms.CharField(max_length=100)
    employee_place=forms.CharField(max_length=100)
    employee_age=forms.CharField(max_length=100)


class Employeemodelform(forms.ModelForm):
    class Meta:
        model=Employeemodel
        fields="__all__"