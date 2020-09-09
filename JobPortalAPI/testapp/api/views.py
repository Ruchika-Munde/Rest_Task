from rest_framework import viewsets
from testapp.models import hydjobs,blorejobs,punejobs,chennaijobs
from testapp.api.serializers import HydjobsSerializer,PunejobsSerializer,BlorejobsSerializer,ChennaidjobsSerializer

class HydJobCRUD(viewsets.ModelViewSet):
    serializer_class = HydjobsSerializer
    queryset = hydjobs.objects.all()

class BloreJobCRUD(viewsets.ModelViewSet):
    serializer_class = BlorejobsSerializer
    queryset = blorejobs.objects.all()

class PuneJobCRUD(viewsets.ModelViewSet):
    serializer_class = PunejobsSerializer
    queryset = punejobs.objects.all()

class ChennaiJobCRUD(viewsets.ModelViewSet):
    serializer_class = ChennaidjobsSerializer
    queryset = chennaijobs.objects.all()