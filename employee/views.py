from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from employee.models import EmployeeModel
from employee.serializers import EmployeeSerializer


class ListCreateEmployeeView(ListCreateAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer


class RetrieveUpdateDestroyEmployeeView(RetrieveUpdateDestroyAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer
