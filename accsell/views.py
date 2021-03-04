from .serializers import accsellSerializers
from rest_framework.views import APIView
from .models import accsell
from accinventory.models import accinventory
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.models import Token



class accsell_create(APIView):
    def post(self,request,format=None):
        serializer=accsellSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            try:
                obj=accinventory.objects.get(branch_code=request.data.get('branch_code'),acc_name=request.data.get('acc_name'))
                obj.quantity-=1
                obj.save()
                return Response('Sold')
            except accinventory.DoesNotExist:
                accinventory.objects.create(branch_code=request.data.get('branch_code'),acc_name=request.data.get('acc_name'),quantity=-1)
                return Response('Sold')
        return Response(serializer.errors)




class accsellsHistory(APIView):
    def get(self,request,format=None,pk=None):
        id=pk
        if id is not None:
            sel=accsell.objects.get(id=id)
            serializer=accsellSerializers(sel)
            tkn=request.META.get('HTTP_AUTHORIZATION')
            return Response(serializer.data)
        sel=accsell.objects.filter(branch_code=request.user.username)
        serializer=accsellSerializers(sel,many=True)
        return Response(serializer.data)