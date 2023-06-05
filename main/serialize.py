from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from main.models import Department, Employee


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        depth = 1
        fields = ['id_employee', 'name', 'photo', 'post', 'salary', 'age', 'id_department']


class DepartmentSerializer(ModelSerializer):
    employee_count = serializers.IntegerField(
        source='employee.count',
        read_only=True
    )

    class Meta:
        model = Department
        fields = ['id_department', 'name_department', 'employee_count', 'boss']

    def to_representation(self, instance):
        result = super(DepartmentSerializer, self).to_representation(instance)
        result["salary_sum"] = sum(
            [person["salary"] for person in EmployeeSerializer(instance.employee, many=True).data])
        return result
