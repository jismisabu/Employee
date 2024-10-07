from rest_framework import serializers

from EMP_app.models import Employeemodel


class Employeeserializer(serializers.ModelSerializer):
    class Meta:
        model=Employeemodel
        fields="__all__"