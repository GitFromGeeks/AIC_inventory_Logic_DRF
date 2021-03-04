from .models import accstock,accinventory
from ledgers.models import ledgers,debth
from accorder.models import acc_order
from acc.models import accessorie
from  .serializers import accinventorySerializers,accstockSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.authtoken.models import Token


class accinventoryView(APIView):
    def get(self,request,format=None,pk=None):
        id=pk
        if id is not None:
            inv=accinventory.objects.filter(branch_code=id)
            serializer=accinventorySerializers(inv)
            tkn=request.META.get('HTTP_AUTHORIZATION')
            return Response(serializer.data)
        inv=accinventory.objects.filter(branch_code=request.user.username)
        serializer=accinventorySerializers(inv,many=True)
        return Response(serializer.data)

class accstockView(APIView):
    def get(self,request,format=None,pk=None):
        id=pk
        mbskt=accstock.objects.all()
        serializer=accstockSerializers(mbskt,many=True)
        return Response(serializer.data)


class accstockCreate(CreateAPIView):
    queryset=accstock.objects.all()
    serializer_class=accstockSerializers
    permission_classes=[IsAdminUser]

    def create(self,request):
        try:
            obj=accstock.objects.get(acc_name==request.data.get('acc_name'))
            obj.quantity+=int(request.data.get('quantity'))
            obj.save()
            return Response("Created")
        except accstock.DoesNotExist:
            nm=request.data.get('acc_name')
            rs=request.data.get('price')
            qty=request.data.get('quantity')
            accstock.objects.create(acc_name=nm,price=rs,quantity=qty,amount=rs*qty)
            return Response("Created")



class accinventoryCreate(CreateAPIView):
    queryset=accinventory.objects.all()
    serializer_class=accinventorySerializers
    permission_classes=[IsAdminUser]


    
    def create(self,request):
        try:
            obj=accinventory.objects.get(branch_code=request.data.get('branch_code'),acc_name=request.data.get('acc_name'))
            obj.quantity+=int(request.data.get('quantity'))
            bc=request.data.get('branch_code')
            acn=request.data.get('acc_name')
            qty=int(request.data.get('quantity'))
            ac=acc.objects.get(acc_name=acn)
            rs=ac.price
            ledgers.objects.create(branch_code=bc,model=" ",quantity=qty,mobile=acn,price=rs,credit=0,debit=qty*rs)
            obj.save()
            ordget=acc_order.objects.get(branch_code=bc,acc_name=acn,quantity=qty)
            ordget.delete()
            try:
                bc=request.data.get("branch_code")
                acn=request.data.get('acc_name')
                qty=int(request.data.get("quantity"))
                ob=debth.objects.get(branch_code=bc)
                ac=acc.objects.get(acc_name=acn)
                rs=ac.price
                debit=rs*qty
                ob.debth+=debit
                ob.save()
                try:
                    acn=request.data.get('acc_name')
                    stk=accstock.objects.get(acc_name=acn)
                    stk.quantity-=int(request.data.get('quantity'))
                    stk.save()
                    return Response("Created")
                except accstock.DoesNotExist:
                    acn=request.data.get('acc_name')
                    qty=-(request.data.get('quantity'))
                    ac=acc.objects.get(acc_name=acn)
                    rs=ac.price
                    accstock.objects.create(acc_name=acn,price=rs,quantity=qty,amount=qty*rs)
                    return Response("Created")               
            except debth.DoesNotExist:
                ac=acc.objects.get(acc_name=acn)
                rs=ac.price
                qty=int(request.data.get("quantity"))
                debit=rs*qty
                debth.objects.create(branch_code=bc,debth=debit)
                try:
                    acn=request.data.get('acc_name')
                    stk=accstock.objects.get(acc_name=acn)
                    stk.quantity-=int(request.data.get('quantity'))
                    stk.save()
                    return Response("Created")
                except accstock.DoesNotExist:
                    acn=request.data.get('acc_name')
                    qty=-(request.data.get('quantity'))
                    ac=acc.objects.get(acc_name=acn)
                    rs=ac.price
                    accstock.objects.create(acc_name=acn,price=rs,quantity=qty,amount=qty*rs)
                    return Response("Created")
        except accinventory.DoesNotExist:
            accinventory.objects.create(branch_code=request.data.get('branch_code'),acc_name=request.data.get('acc_name'),quantity=int(request.data.get('quantity')))
            bc=request.data.get('branch_code')
            acn=request.data.get('acc_name')
            qty=int(request.data.get('quantity'))
            ac=acc.objects.get(acc_name=acn)
            rs=ac.price
            ledgers.objects.create(branch_code=bc,model=" ",quantity=qty,mobile=acn,price=rs,credit=0,debit=qty*rs)
            ordget=acc_order.objects.get(branch_code=bc,acc_name=acn,quantity=qty)
            ordget.delete()
            try:
                bc=request.data.get("branch_code")
                acn=request.data.get('acc_name')
                qty=int(request.data.get("quantity"))
                ob=debth.objects.get(branch_code=bc)
                ac=acc.objects.get(acc_name=acn)
                rs=ac.price
                debit=rs*qty
                ob.debth+=debit
                ob.save()
                try:
                    acn=request.data.get('acc_name')
                    stk=accstock.objects.get(acc_name=acn)
                    stk.quantity-=int(request.data.get('quantity'))
                    stk.save()
                    return Response("Created")
                except accstock.DoesNotExist:
                    acn=request.data.get('acc_name')
                    qty=-(request.data.get('quantity'))
                    ac=acc.objects.get(acc_name=acn)
                    rs=ac.price
                    accstock.objects.create(acc_name=acn,price=rs,quantity=qty,amount=qty*rs)
                    return Response("Created")
            except debth.DoesNotExist:
                ac=acc.objects.get(acc_name=acn)
                rs=ac.price
                qty=int(request.data.get("quantity"))
                debit=rs*qty
                debth.objects.create(branch_code=bc,debth=debit)
                try:
                    acn=request.data.get('acc_name')
                    stk=accstock.objects.get(acc_name=acn)
                    stk.quantity-=int(request.data.get('quantity'))
                    stk.save()
                    return Response("Created")
                except accstock.DoesNotExist:
                    acn=request.data.get('acc_name')
                    qty=-(request.data.get('quantity'))
                    ac=acc.objects.get(acc_name=acn)
                    rs=ac.price
                    accstock.objects.create(acc_name=acn,price=rs,quantity=qty,amount=qty*rs)
                    return Response("Created")