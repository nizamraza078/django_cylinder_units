from rest_framework import serializers
from .models import User_info
class User_info_serializer(serializers.ModelSerializer):
    class Meta:
        model=User_info
        fields='__all__'
    def create(self,validated_data):
        user=User_info.objects.create(Address=validated_data['Address'],Businessname=validated_data['Businessname'],Person_name=validated_data['Person_name'],contact=validated_data['contact'],verifiedstatus=validated_data['verifiedstatus'])
        return user