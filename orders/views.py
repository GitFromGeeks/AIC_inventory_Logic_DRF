from django.shortcuts import render
import io
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import ordersSerializer
from rest_framework.generics import ListAPIView
from .models import orders

@csrf_exempt
def order_create(request):
    if request.method =='post':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=ordersSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            return


class orderHistory(ListAPIView):
    queryset=orders.objects.all()
    serializer_class=ordersSerializer