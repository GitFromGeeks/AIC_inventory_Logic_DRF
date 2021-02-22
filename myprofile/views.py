from django.shortcuts import render
from .serializers import myprofileSerializers
from rest_framework.views import APIView
from .models import myprofile
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.response import Response



class myprofileView(APIView):
    def get(self,request,pk=None,format=None):
        id=pk
        tkn=request.META.get('HTTP_AUTHORIZATION')
        pro=myprofile.objects.get(branch_code=request.user.username)
        serializer=myprofileSerializers(pro)
        return Response(serializer.data)