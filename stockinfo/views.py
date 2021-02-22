from django.shortcuts import render
from .serializers import stockinfoSerializers
from rest_framework.views import APIView
from .models import stockinfo
from rest_framework.response import Response
from rest_framework.authtoken.models import Token




class stockinfoView(APIView):
    def get(self,request,format=None,pk=None):
        id=pk
        if id is not None:
            stk=stockinfo.objects.get(id=id)
            serializer=stockinfoSerializers(stk)
            tkn=request.META.get('HTTP_AUTHORIZATION')
            return Response(serializer.data)
        stk=stockinfo.objects.filter(branch_code=request.user.username)
        serializer=stockinfoSerializers(stk,many=True)
        return Response(serializer.data)