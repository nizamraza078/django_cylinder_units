from django.shortcuts import render

# Create your views here
from rest_framework.parsers import  JSONParser
from rest_framework.renderers import  JSONRenderer
from .models import User_info
from .serializer import User_info_serializer
from django.http import HttpResponse
import io
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import  Response

class Oxygen_cylinder_view(APIView):
    serializer_class=User_info_serializer
    def get(self,request,format=None):
        return Response({'message':'Hello'})
    def post(self,request):
        json_data=request.body
        stream_data_val=io.BytesIO(json_data)
        data_parse=JSONParser().parse(stream_data_val)
        serializer_val=User_info_serializer(data=data_parse)
        if(serializer_val.is_valid()):
            serializer_val.save()
            message={'message':'Resource created'}
            json_data=JSONRenderer().render(message)
            return HttpResponse(json_data,content_type='application/json')
class User_view_set(viewsets.ModelViewSet):
    serializer_class = User_info_serializer
    queryset = User_info.objects.all()




