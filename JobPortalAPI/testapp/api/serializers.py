from rest_framework.serializers import ModelSerializer
from testapp.models import hydjobs,chennaijobs,punejobs,blorejobs

class HydjobsSerializer(ModelSerializer):
    class Meta:
        model=hydjobs
        fields='__all__'

class BlorejobsSerializer(ModelSerializer):
    class Meta:
        model=blorejobs
        fields='__all__'

class PunejobsSerializer(ModelSerializer):
    class Meta:
        model=punejobs
        fields='__all__'

class ChennaidjobsSerializer(ModelSerializer):
    class Meta:
        model=chennaijobs
        fields='__all__'