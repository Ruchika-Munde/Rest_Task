from django.shortcuts import render
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.viewsets import ModelViewSet

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly

from testapp.permissions import IsReadOnly
# Create your views here.

class EmployeeCRUDCBV(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [TokenAuthentication, ]

#  *** IsAutheticated - Enabling Locally Authetication and Authorization
    # permission_classes = [IsAuthenticated,]

# *** AllowAny - permission for if dont want authorization when Enable globally
    # permission_classes = [AllowAny,]

# *** IsAdmiUser - only admin is allowed
#     permission_classes = [IsAdminUser,]

# *** IsAuthenticatedOrReadOnly
    #permission_classes = [IsAuthenticatedOrReadOnly,]

# ***DjangoModelPermission
#     permission_classes = [DjangoModelPermissions,]

#*** for customize permissions create permissions.py file
# ***Customise permission For safe methods i.e. GET,HEAD,OPTIONS
    permission_classes = [IsReadOnly,]