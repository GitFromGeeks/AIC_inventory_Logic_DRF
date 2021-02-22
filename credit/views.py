from django.shortcuts import render
from .models import credit
from ledgers.models import ledgers,debth
from .serializers import creditSerializers
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser



class credit_create(CreateAPIView):
    queryset=credit.objects.all()
    serializer_class=creditSerializers
    permission_classes=[IsAdminUser]


    def create(self,request):
        try:
            bc=request.data.get("branch_code")
            ob=debth.objects.get(branch_code=bc)
            cdt=int(request.data.get('credit'))
            ob.debth-=cdt
            ob.save()
            dcs=request.data.get('description')
            ledgers.objects.create(branch_code=bc,model='---',quantity=1,mobile=dcs,price=0,credit=cdt,debit=0)
            return Response({'msg':'Payment Accepted'})
        except debth.DoesNotExist:
            cdt=-int(request.data.get('credit'))
            bc=request.data.get("branch_code")
            debth.objects.create(branch_code=bc,debth=cdt)
            dcs=request.data.get('description')
            ledgers.objects.create(branch_code=bc,model='---',quantity=1,mobile=dcs,price=0,credit=cdt,debit=0)
            return Response({'msg':'Payment Accepted'})


