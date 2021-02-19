from django.shortcuts import render
from .models import inventory
from ledgers.models import ledgers,debth
from orders.models import orders
from phone.models import phone
from  .serializers import inventorySerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser

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
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAdminUser]


    
    def create(self,request):
        try:
            obj=inventory.objects.get(branch_code=request.data.get('branch_code'),model=request.data.get('model'))
            obj.quantity+=int(request.data.get('quantity'))
            bc=request.data.get('branch_code')
            md=request.data.get('model')
            qty=int(request.data.get('quantity'))
            ph=phone.objects.get(model=md)
            mbl=ph.mobile
            rs=ph.price
            ledgers.objects.create(branch_code=bc,model=md,quantity=qty,mobile=mbl,price=rs,credit=0,debit=qty*rs)
            obj.save()
            ordget=orders.objects.get(branch_code=bc,model=md,quantity=qty)
            ordget.delete()
            try:
                bc=request.data.get("branch_code")
                md=request.data.get('model')
                qty=int(request.data.get("quantity"))
                ob=debth.objects.get(branch_code=bc)
                ph=phone.objects.get(model=md)
                rs=ph.price
                debit=rs*qty
                ob.debth+=debit
                ob.save()
                return Response("")
            except debth.DoesNotExist:
                ph=phone.objects.get(model=md)
                rs=ph.price
                qty=int(request.data.get("quantity"))
                debit=rs*qty
                debth.objects.create(branch_code=bc,debth=debit)
                return Response("")

        except inventory.DoesNotExist:
            inventory.objects.create(branch_code=request.data.get('branch_code'),model=request.data.get('model'),mobile=request.data.get('mobile'),quantity=int(request.data.get('quantity')))
            bc=request.data.get('branch_code')
            md=request.data.get('model')
            qty=int(request.data.get('quantity'))
            ph=phone.objects.get(model=md)
            mbl=ph.mobile
            rs=ph.price
            ledgers.objects.create(branch_code=bc,model=md,quantity=qty,mobile=mbl,price=rs,credit=0,debit=qty*rs)
            ordget=orders.objects.get(branch_code=bc,model=md,quantity=qty)
            ordget.delete()
            try:
                bc=request.data.get("branch_code")
                md=request.data.get('model')
                qty=int(request.data.get("quantity"))
                ob=debth.objects.get(branch_code=bc)
                ph=phone.objects.get(model=md)
                rs=ph.price
                debit=rs*qty
                ob.debth+=debit
                ob.save()
                return Response("")
            except debth.DoesNotExist:
                debth.objects.create(branch_code=bc,debth=debit)
                return Response("")
    
