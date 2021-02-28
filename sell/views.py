from .serializers import sellSerializers
from rest_framework.views import APIView
from .models import sell
from inventory.models import inventory
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.models import Token



class sell_create(APIView):
    def post(self,request,format=None):
        serializer=sellSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            try:
                obj=inventory.objects.get(branch_code=request.data.get('branch_code'),model=request.data.get('model'))
                obj.quantity-=1
                obj.save()
                return Response('Sold')
            except inventory.DoesNotExist:
                inventory.objects.create(branch_code=request.data.get('branch_code'),model=request.data.get('model'),mobile=request.data.get('mobile'),quantity=-1)
                return Response('Sold')
        return Response(serializer.errors)




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