from django.shortcuts import render
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from testapp.permissions import IsReadOnly, IsGETorPATCH,ruchaPermission
# Create your views here.

class EmployeeCRUD(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [TokenAuthentication,]

# ***IsReadOnly() - SAFE_METHOD i.e.(GET/OPTIONS/HEAD)
    #permission_classes = [IsReadOnly,]

# ***GET-PATCH() method
#     permission_classes = [IsGETorPATCH,]

# ***rucha permission  class
    permission_classes = [ruchaPermission,]