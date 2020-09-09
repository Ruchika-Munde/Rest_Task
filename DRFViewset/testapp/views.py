from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from testapp.serializers import NameSerializer
# Create your views here.

class TestViewset(ViewSet):
    def list(self,request):
        colors=['blue','red','green','yellow']
        return Response({'msg':'Happy Holi','colors':colors})

    def create(self,request):
        serializer=NameSerializer(data=request.data)
        if serializer.is_valid():
            name=serializer.data.get('name')
            msg='Hello {} happy new year !!!'.format(name)
            return Response({'msg':msg})
        else:
            return Response(serializer.errors,status=400)

    def retrieve(self,request,pk=None):
        return Response({'msg':'This is Response from RETRIEVE method'})

    def update(self,request,pk=None):
        return Response({'msg':'This is Response from UPDATE method'})

    def partial_update(self,request,pk=None):
        return Response({'msg':'This is Response from PARTIAL_UPDATE method'})

    def destroy(self,request,pk=None):
        return Response({'msg':'This is Response from DESTROY method'})
