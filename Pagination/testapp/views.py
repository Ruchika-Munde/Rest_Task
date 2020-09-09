from django.shortcuts import render
from testapp.serializers import  EmployeeSerializer
from testapp.models import Employee
from testapp.pagination1 import MyPagination
from rest_framework import generics
# Create your views here.

class EmployeeAPIView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = MyPagination