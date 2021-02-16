from django.shortcuts import render
import io
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import sellSerializers
from rest_framework.generics import ListAPIView
from .models import sell

@csrf_exempt
def sell_create(request):
    if request.method =='post':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=ordersSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            return


class sellsHistory(ListAPIView):
    queryset=sell.objects.all()
    serializer_class=sellSerializers