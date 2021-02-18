from django.shortcuts import render
from .models import inventory
from ledgers.models import ledgers
from phone.models import phone
from  .serializers import inventorySerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView


class inventoryView(APIView):
    def get(self,request,format=None,pk=None):
        id=pk
        if id is not None:
            inv=inventory.objects.get(id=id)
            serializer=inventorySerializers(inv)
            return Response(serializer.data)
        inv=inventory.objects.filter(branch_code=request.user.username)
        serializer=inventorySerializers(inv,many=True)
        return Response(serializer.data)



class inventoryCreate(CreateAPIView):
    queryset=inventory.objects.all()
    serializer_class=inventorySerializers

    def create(self,request):
        try:
            obj=inventory.objects.get(branch_code=request.user.username,model=request.data.get('model'))
            obj.quantity+=int(request.data.get('quantity'))
            bc=request.user.username
            md=request.data.get('model')
            qty=int(request.data.get('quantity'))
            ph=phone.objects.get(model=md)
            mbl=ph.mobile
            rs=ph.price
            ledgers.objects.create(branch_code=bc,model=md,quantity=qty,mobile=mbl,price=rs,credit=0,debit=qty*rs)
            obj.save()
            return Response('')
        except inventory.DoesNotExist:
            inventory.objects.create(branch_code=request.user.username,model=request.data.get('model'),mobile=request.data.get('mobile'),quantity=int(request.data.get('quantity')))
            bc=request.user.username
            md=request.data.get('model')
            qty=int(request.data.get('quantity'))
            ph=phone.objects.get(model=md)
            mbl=ph.mobile
            rs=ph.price
            ledgers.objects.create(branch_code=bc,model=md,quantity=qty,mobile=mbl,price=rs,credit=0,debit=qty*rs)
            return Response('')