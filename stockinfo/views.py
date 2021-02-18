from django.shortcuts import render
from .serializers import stockinfoSerializers
from rest_framework.views import APIView
from .models import stockinfo
from rest_framework.response import Response





class stockinfoView(APIView):
    def get(self,request,format=None,pk=None):
        id=pk
        if id is not None:
            stk=stockinfo.objects.get(id=id)
            serializer=stockinfoSerializers(stk)
            return Response(serializer.data)
        stk=stockinfo.objects.filter(branch_code=request.user.username)
        serializer=stockinfoSerializer(stk,many=True)
        return Response(serializer.data)