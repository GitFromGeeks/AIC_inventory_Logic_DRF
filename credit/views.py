from django.shortcuts import render
from .models import credit
import io
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import creditSerializers


@csrf_exempt
def credit_create(request):
    if request.method =='post':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=creditSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            return