from django.shortcuts import render
from .models import credit
from ledgers.models import ledgers
from .serializers import creditSerializers
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView


class credit_create(APIView):
    def post(self, request, format=None):
        serializer = creditSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            bc=request.data.get('branch_code')
            cdt=request.data.get('credit')
            dcs=request.data.get('description')
            ledgers.objects.create(branch_code=bc,model='---',quantity=1,mobile=dcs,price=0,credit=cdt,debit=0)
            return Response({'msg':'Payment Accepted'})
        return Response(serializer.errors)
