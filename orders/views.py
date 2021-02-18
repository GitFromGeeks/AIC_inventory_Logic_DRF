from django.shortcuts import render
import io
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import ordersSerializer
from rest_framework.views import APIView
from .models import orders
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView

class order_create(CreateAPIView):
    queryset=orders.objects.all()
    serializer_class=ordersSerializer

# @csrf_exempt
# def order_create(request):
#     if request.method =='post':
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         pythondata=JSONParser().parse(stream)
#         serializer=ordersSerializer(data=pythondata)
#         if serializer.is_valid():
#             serializer.save()
#             return Response('')


class orderHistory(APIView):
    def get(self,request,format=None,pk=None):
        id=pk
        if id is not None:
            ord=orders.objects.get(id=id)
            serializer=ordersSerializers(ord)
            return Response(serializer.data)
        ord=orders.objects.filter(branch_code=request.user.username)
        serializer=ordersSerializer(ord,many=True)
        return Response(serializer.data)