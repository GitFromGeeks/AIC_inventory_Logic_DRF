import io
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import accSerializer
from rest_framework.views import APIView
from .models import acc_order
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.models import Token

class accorder_create(CreateAPIView):
    queryset=acc_order.objects.all()
    serializer_class=accSerializer

class accorderHistory(APIView):
    def get(self,request,format=None,pk=None):
        id=pk
        if id is not None:
            ord=acc_order.objects.get(id=id)
            serializer=accSerializer(ord)
            tkn=request.META.get('HTTP_AUTHORIZATION')
            return Response(serializer.data)
        acord=acc_order.objects.filter(branch_code=request.user.username)
        serializer=accSerializer(acord,many=True)
        return Response(serializer.data)



class accorderdelete(APIView):
    def get(self,request,pk,format=None):
        id=pk
        acord1=acc_order.objects.get(pk=id)
        acord1.delete()
        return Response('Deleted')


class accinventoryadd(APIView):
    def get(self,request,format=None,pk=None):
        id=pk
        if id is not None:
            acord=acc_order.objects.get(id=id)
            serializer=accSerializer(ord)
            return Response(serializer.data)
        acord=acc_order.objects.all()
        serializer=accSerializer(acord,many=True)
        return Response(serializer.data)
