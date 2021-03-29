from rest_framework.serializers import ModelSerializer

from .models import CompanyModel
from employee.serializers import EmployeeSerializer


class CompanySerializer(ModelSerializer):
    employee = EmployeeSerializer(many=True, required=False)

    class Meta:
        model = CompanyModel
        fields = '__all__'
