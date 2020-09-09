from django.shortcuts import render
from testapp.models import Employee
from testapp.serializer import EmployeeSerializer
from rest_framework.mixins import *
from rest_framework.generics import ListAPIView,RetrieveAPIView
# Create your views here.

class EmployeeListModelMixin(CreateModelMixin,ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs) # this create is coming from parent class i.e. CreateModelMixin

class EmployeeRetrieveupdateDestroyModelMixin(RetrieveAPIView,UpdateModelMixin,DestroyModelMixin):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def patch(self,request,*args,**kwargs):
        return self.partial_update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)