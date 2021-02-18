from django.shortcuts import render
from .serializers import sellSerializers
from rest_framework.views import APIView
from .models import sell
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView


class sell_create(CreateAPIView):
    queryset=sell.objects.all()
    serializer_class=sellSerializers


class sellsHistory(APIView):
    def get(self,request,format=None,pk=None):
        id=pk
        if id is not None:
            sel=sell.objects.get(id=id)
            serializer=sellSerializers(sel)
            return Response(serializer.data)
        sel=sell.objects.filter(branch_code=request.user.username)
        serializer=sellSerializers(sel,many=True)
        return Response(serializer.data)