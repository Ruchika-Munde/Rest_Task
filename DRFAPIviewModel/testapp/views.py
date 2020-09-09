from django.shortcuts import render
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView,RetrieveDestroyAPIView
# Create your views here.

# class EmployeeListAPIView(APIView):
#     def get(self,request,format=None):
#         qs=Employee.objects.all()
#         serializer=EmployeeSerializer(qs,many=True)
#         return Response(serializer.data )

class EmployeeListAPIView(ListAPIView): #get() method i.e. fetch all records
    queryset = Employee.objects.all()   #queryset and serializer_class is predefined name given by rest_framework.generic API classes
    serializer_class = EmployeeSerializer

    def get_queryset(self): # for search operations
           qs=Employee.objects.all()
           name=self.request.GET.get('ename')
           if name is not None:
               qs=qs.filter(ename__icontains=name)
           return qs

class EmployeeCreateAPIView(CreateAPIView):   # post() method
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeRetriveAPIView(RetrieveAPIView):  # get() i.e. fetch perticular record
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # lookup_field = 'id' # write this code when use in url id instead of pk

class EmployeeUpdateAPIView(UpdateAPIView):  # put(), patch() method
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDeleteAPIView(DestroyAPIView):  # delete() method
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeListCreateView(ListCreateAPIView): # get(),post() method             # 2 end points
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeRetrieveUpdateView(RetrieveUpdateAPIView): #get() perticular data, put,patch() method
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeRetrieveDestroyView(RetrieveDestroyAPIView): #get() perticular record, delete() method
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):  #get() perticular record, put()-patch(), delete()         # 2 end points
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

