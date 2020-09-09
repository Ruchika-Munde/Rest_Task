from rest_framework import serializers
from testapp.models import Employee

def multiples_of_1000(value):
    if value %100 !=0:
        raise serializers.ValidationError('Salary should be multiple of 1000')
class EmployeeSerializer(serializers.Serializer): #normal serializer
    eno = serializers.IntegerField()
    ename = serializers.CharField(max_length=64)
    esal = serializers.FloatField(validators=[multiples_of_1000,])
    eaddr = serializers.CharField(max_length=64)

    '''field level validation'''
    def validate_esal(self,value):
        if value<5000:
            raise serializers.ValidationError('Employee salary should be minimum 5000')
        return value

    '''object level validation'''
    def validate(self,data):
        ename=data.get('ename')
        esal=data.get('esal')
        if ename.lower()=='rucha':
            if esal<50000:
                raise serializers.ValidationError('Rucha salary should be 50000')
        return data
    '''create a data post()'''
    def create(self,validated_data):
        return Employee.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.eno=validated_data.get('eno',instance.eno)
        instance.ename=validated_data.get('ename',instance.ename)
        instance.esal=validated_data.get('esal',instance.esal)
        instance.eaddr=validated_data.get('eaddr',instance.eaddr)
        instance.save()
        return instance