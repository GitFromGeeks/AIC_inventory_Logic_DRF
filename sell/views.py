from .serializers import sellSerializers
from rest_framework.views import APIView
from .models import sell
from django.http import HttpResponse
from inventory.models import inventory
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
import datetime
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
# from django.db.models import Sum
from phone.models import phone
from ledgers.models import ledgers,debth

class export_pdf(APIView):
    permission_classes=[AllowAny]
    def get(self,request,format=None,pk=None):
        id=pk
        response=HttpResponse(content_type='application/pdf')
        response['Content-Disposition']='inline; attachment; filename=Sell'+\
            str(datetime.datetime.now())+'.pdf'
        response['Content-Transfer-Encoding']='binary'
        sells=sell.objects.filter(branch_code=id)
        html_string=render_to_string('pdfoutput.html',{'sells':sells,'total':0,'bcode':id})
        html=HTML(string=html_string)
        result=html.write_pdf()
        with tempfile.NamedTemporaryFile(delete=True) as output:
            output.write(result)
            output.flush()
            output=open(output.name,'rb')
            response.write(output.read())
        return response


class sell_create(APIView):
    def post(self,request,format=None):
        serializer=sellSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            try:
                obj=inventory.objects.get(branch_code=request.data.get('branch_code'),model=request.data.get('model'))
                obj.quantity-=1
                obj.save()
                phn=phone.objects.get(model=request.data.get('model'))
                rs=int(phn.price)
                mb=phn.mobile
                ob=debth.objects.get(branch_code=request.data.get('branch_code'))
                ob.debth-=rs
                ob.save()
                ledgers.objects.create(branch_code=request.data.get('branch_code'),model=request.data.get('model'),quantity=1,mobile=mb,price=0,credit=rs,debit=0)
                return Response('Sold')
            except inventory.DoesNotExist:
                inventory.objects.create(branch_code=request.data.get('branch_code'),model=request.data.get('model'),mobile=request.data.get('mobile'),quantity=-1)
                return Response('Sold')
        return Response(serializer.errors)


class sellsview(ListAPIView):
    queryset=sell.objects.all()
    serializer_class=sellSerializers

class sellsHistory(APIView):
    def get(self,request,format=None,pk=None):
        id=pk
        if id is not None:
            sel=sell.objects.get(id=id)
            serializer=sellSerializers(sel)
            tkn=request.META.get('HTTP_AUTHORIZATION')
            return Response(serializer.data)
        sel=sell.objects.filter(branch_code=request.user.username)
        serializer=sellSerializers(sel,many=True)
        return Response(serializer.data)