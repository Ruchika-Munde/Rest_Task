from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from testapp.serializers import NameSerializer
# Create your views here.

class TestAPIView(APIView):
    def get(self,request,*args,**kwargs):
        colors=['RED','Green','Yellow','Blue']
        return Response({'msg':'Happy Holi','colors':colors})

    def post(self,request,*args,**kwargs):
        serializer=NameSerializer(data=request.data)
        if serializer.is_valid():
            name=serializer.data.get('name')
            msg='Hello {} Happy Holi !!!'.format(name)
            return Response({'msg':msg})

        else:
            return Response(serializer.errors,status=400)

    def put(self,request,*args,**kwargs):
        return Response({"msg":'This response from PUT method'})

    def patch(self,request,*args,**kwargs):
        return Response({"msg":'This response from PATCH method'})

    def delete(self,request,*args,**kwargs):
        return Response({"msg":'This response from DELETE method'})

