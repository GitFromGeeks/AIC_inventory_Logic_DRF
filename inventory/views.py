from .models import inventory,mobilestock,transferstock
from ledgers.models import ledgers,debth
from orders.models import orders
from phone.models import phone
from  .serializers import inventorySerializers,mobilestockSerializers,transferstockSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.filters import SearchFilter
import datetime
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
from django.http import HttpResponse


class export_pdfinv(APIView):
    permission_classes=[AllowAny]
    def get(self,request,format=None,pk=None):
        id=pk
        response=HttpResponse(content_type='application/pdf')
        response['Content-Disposition']='inline; attachment; filename=Inventory'+\
            str(datetime.datetime.now())+'.pdf'
        response['Content-Transfer-Encoding']='binary'
        inven=inventory.objects.filter(branch_code=id)
        html_string=render_to_string('inventoryinfo.html',{'inven':inven,'total':0,'bcode':id})
        html=HTML(string=html_string)
        result=html.write_pdf()
        with tempfile.NamedTemporaryFile(delete=True) as output:
            output.write(result)
            output.flush()
            output=open(output.name,'rb')
            response.write(output.read())
        return response


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

class transferinfoView(ListAPIView):
    queryset=transferstock.objects.all()
    serializer_class=transferstockSerializers


class branchinventoryView(ListAPIView):
    queryset=inventory.objects.all()
    serializer_class=inventorySerializers
    filter_backends=[SearchFilter]
    search_fields=['^branch_code']

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


class Returnstock(APIView):
    def post(self,request,format=None):
        obj=inventory.objects.get(branch_code=request.data.get('branch_code'),model=request.data.get('model'))
        obj.quantity-=1
        obj.save()
        phn=phone.objects.get(model=request.data.get('model'))
        rs=phn.price
        dbt=debth.objects.get(branch_code=request.data.get('branch_code'))
        dbt.debth-=rs
        dbt.save()
        mbstk=mobilestock.objects.get(model=request.data.get('model'))
        mbstk.quantity+=1
        mbstk.save()
        return Response('Returned')


class transfer(APIView):
    def post(self,request,format=None):
        obj=inventory.objects.get(branch_code=request.data.get('branch_code1'),model=request.data.get('model'))
        obj.quantity-=1
        obj.save()
        phn=phone.objects.get(model=request.data.get('model'))
        rs=phn.price
        dbt=debth.objects.get(branch_code=request.data.get('branch_code1'))
        dbt.debth-=rs
        dbt.save()
        transferstock.objects.create(frombranch=request.data.get('branch_code1'),tobranch=request.data.get('branch_code2'),model=request.data.get('model'))
        try:
            ob=inventory.objects.get(branch_code=request.data.get('branch_code2'),model=request.data.get('model'))
            ob.quantity+=1
            ob.save()
            ph=phone.objects.get(model=request.data.get('model'))
            rs=ph.price
            dbt1=debth.objects.get(branch_code=request.data.get('branch_code2'))
            dbt1.debth+=rs
            dbt1.save()
            return Response('Transfer done')
        except inventory.DoesNotExist:
            phn=phone.objects.get(model=request.data.get('model'))
            mbl=phn.mobile
            inventory.objects.create(branch_code=request.data.get('branch_code2'),model=request.data.get('model'),mobile=mbl,quantity=1)
            dbt1=debth.objects.get(branch_code=request.data.get('branch_code2'))
            dbt1.debth+=rs
            dbt1.save()
            return Response('Transfer done')


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
