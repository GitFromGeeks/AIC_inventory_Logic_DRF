from django.shortcuts import render
from .serializers import ledgersSerializers,debthSerializers
from .models import ledgers,debth
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser




class ledgersView(APIView):
    def get(self,request,format=None,pk=None):
        id=pk
        if id is not None:
            led=ledgers.objects.get(id=id)
            serializer=ledgersSerializers(led)
            return Response(serializer.data)
        led=ledgers.objects.filter(branch_code=request.user.username)
        serializer=ledgersSerializers(led,many=True)
        return Response(serializer.data)




class AICdebthView(APIView):
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAdminUser]
    def get(self,request,format=None,pk=None):
        branch_code=pk
        if branch_code is not None:
            dt=debth.objects.get(branch_code=branch_code)
            serializer=debthSerializers(dt)
            return Response(serializer.data)
        dt=debth.objects.all()
        serializer=debthSerializers(dt,many=True)
        return Response(serializer.data)



class debthView(APIView):
    def get(self,request,format=None,pk=None):
        branch_code=pk
        if branch_code is not None:
            dt=debth.objects.get(branch_code=branch_code)
            serializer=debthSerializers(dt)
            return Response(serializer.data)
        dt=debth.objects.filter(branch_code=request.user.username)
        serializer=debthSerializers(dt,many=True)
        return Response(serializer.data)