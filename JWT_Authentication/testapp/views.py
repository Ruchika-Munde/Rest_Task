from django.shortcuts import render
from testapp.serializers import EmployeeSerializer
from testapp.models import Employee
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from testapp.authentication import CustomAuthentication,CustomAuthentication2
# Create your views here.

class EmployeeCRUD(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

#*** JWT authentication
    # authentication_classes = [JSONWebTokenAuthentication,]

# *** Customise authentication
#     authentication_classes = [CustomAuthentication,]

# ***Customise Authentication2
    authentication_classes = [CustomAuthentication2,]
    permission_classes = [IsAuthenticated,]