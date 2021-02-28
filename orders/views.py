import io
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import ordersSerializer
from rest_framework.views import APIView
from .models import orders
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.models import Token

class order_create(CreateAPIView):
    queryset=orders.objects.all()
    serializer_class=ordersSerializer




class orderHistory(APIView):
    def get(self,request,format=None,pk=None):
        id=pk
        if id is not None:
            ord=orders.objects.get(id=id)
            serializer=ordersSerializer(ord)
            tkn=request.META.get('HTTP_AUTHORIZATION')
            return Response(serializer.data)
        ord=orders.objects.filter(branch_code=request.user.username)
        serializer=ordersSerializer(ord,many=True)
        return Response(serializer.data)



class orderdelete(APIView):
    def get(self,request,pk,format=None):
        id=pk
        ord1=orders.objects.get(pk=id)
        ord1.delete()
        return Response('Deleted')


class inventoryadd(APIView):
    def get(self,request,format=None,pk=None):
        id=pk
        if id is not None:
            ord=orders.objects.get(id=id)
            serializer=ordersSerializer(ord)
            return Response(serializer.data)
        ord=orders.objects.all()
        serializer=ordersSerializer(ord,many=True)
        return Response(serializer.data)
