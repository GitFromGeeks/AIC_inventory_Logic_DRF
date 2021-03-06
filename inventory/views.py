from .models import inventory,mobilestock
from ledgers.models import ledgers,debth
from orders.models import orders
from phone.models import phone
from  .serializers import inventorySerializers,mobilestockSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.authtoken.models import Token


class inventoryView(APIView):
    def get(self,request,format=None,pk=None):
        id=pk
        if id is not None:
            inv=inventory.objects.filter(branch_code=id)
            serializer=inventorySerializers(inv)
            tkn=request.META.get('HTTP_AUTHORIZATION')
            return Response(serializer.data)
        inv=inventory.objects.filter(branch_code=request.user.username)
        serializer=inventorySerializers(inv,many=True)
        return Response(serializer.data)

class mobilestockView(APIView):
    def get(self,request,format=None,pk=None):
        id=pk
        mbskt=mobilestock.objects.all()
        serializer=mobilestockSerializers(mbskt,many=True)
        return Response(serializer.data)


class mobilestockCreate(CreateAPIView):
    queryset=mobilestock.objects.all()
    serializer_class=mobilestockSerializers
    permission_classes=[IsAdminUser]

    def create(self,request):
        try:
            md=request.data.get('model')
            obj=mobilestock.objects.get(model=request.data.get('model'))
            qty=int(request.data.get('quantity'))
            obj.quantity+=qty
            ph=phone.objects.get(model=md)
            rs=ph.price
            amnt=rs*qty
            obj.amount+=amnt
            obj.save()
            return Response("Created")
        except mobilestock.DoesNotExist:
            md=request.data.get('model')
            mb=request.data.get('mobile')
            rs=request.data.get('price')
            qty=request.data.get('quantity')
            mobilestock.objects.create(model=md,mobile=mb,price=rs,quantity=qty,amount=qty*rs)
            return Response("Created")




class inventoryCreate(CreateAPIView):
    queryset=inventory.objects.all()
    serializer_class=inventorySerializers
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
                try:
                    md=request.data.get('model')
                    qty=int(request.data.get('quantity'))
                    mbstk=mobilestock.objects.get(model=md)
                    mbstk.quantity-=qty
                    ph=phone.objects.get(model=md)
                    rs=ph.price
                    amtm=qty*rs
                    mbstk.amount-=amtm
                    mbstk.save()
                    return Response('Created')
                except mobilestock.DoesNotExist:
                    md=request.data.get('model')
                    qty=request.data.get('quantity')
                    ph=phone.objects.get(model=md)
                    mbl=ph.mobile
                    rs=ph.price
                    mobilestock.objects.create(model=md,mobile=mbl,price=rs,quantity=-qty,amount=-qty*rs)
                    return Response('Created')
            except debth.DoesNotExist:
                ph=phone.objects.get(model=md)
                rs=ph.price
                qty=int(request.data.get("quantity"))
                debit=rs*qty
                debth.objects.create(branch_code=bc,debth=debit)
                try:
                    md=request.data.get('model')
                    qty=int(request.data.get('quantity'))
                    mbstk=mobilestock.objects.get(model=md)
                    mbstk.quantity-=qty
                    ph=phone.objects.get(model=md)
                    rs=ph.price
                    amtm=qty*rs
                    mbstk.amount-=amtm
                    mbstk.save()
                    return Response('Created')
                except mobilestock.DoesNotExist:
                    md=request.data.get('model')
                    qty=request.data.get('quantity')
                    ph=phone.objects.get(model=md)
                    mbl=ph.mobile
                    rs=ph.price
                    mobilestock.objects.create(model=md,mobile=mbl,price=rs,quantity=-qty,amount=-qty*rs)
                    return Response('Created')
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
                try:
                    md=request.data.get('model')
                    qty=int(request.data.get('quantity'))
                    mbstk=mobilestock.objects.get(model=md)
                    mbstk.quantity-=qty
                    ph=phone.objects.get(model=md)
                    rs=ph.price
                    amtm=qty*rs
                    mbstk.amount-=amtm
                    mbstk.save()
                    return Response('Created')
                except mobilestock.DoesNotExist:
                    md=request.data.get('model')
                    qty=request.data.get('quantity')
                    ph=phone.objects.get(model=md)
                    mbl=ph.mobile
                    rs=ph.price
                    mobilestock.objects.create(model=md,mobile=mbl,price=rs,quantity=-qty,amount=-qty*rs)
                    return Response('Created')
            except debth.DoesNotExist:
                debth.objects.create(branch_code=bc,debth=debit)
                try:
                    md=request.data.get('model')
                    qty=int(request.data.get('quantity'))
                    mbstk=mobilestock.objects.get(model=md)
                    mbstk.quantity-=qty
                    ph=phone.objects.get(model=md)
                    rs=ph.price
                    amtm=qty*rs
                    mbstk.amount-=amtm
                    mbstk.save()
                    return Response('Created')
                except mobilestock.DoesNotExist:
                    md=request.data.get('model')
                    qty=request.data.get('quantity')
                    ph=phone.objects.get(model=md)
                    mbl=ph.mobile
                    rs=ph.price
                    mobilestock.objects.create(model=md,mobile=mbl,price=rs,quantity=-qty,amount=-qty*rs)
                    return Response('Created')
