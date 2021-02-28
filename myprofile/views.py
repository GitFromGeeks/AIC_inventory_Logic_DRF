from django.shortcuts import render
from .serializers import myprofileSerializers
from rest_framework.views import APIView
from .models import myprofile
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter



# class myprofileView(APIView):
#     def get(self,request,pk=None,format=None):
#         id=pk
#         tkn=request.META.get('HTTP_AUTHORIZATION')
#         pro=myprofile.objects.get(branch_code=request.user.username)
#         serializer=myprofileSerializers(pro)
#         return Response(serializer.data)


class myprofileView(ListAPIView):
    queryset=myprofile.objects.all()
    serializer_class=myprofileSerializers
    filter_backends=[SearchFilter]
    search_fields=['^branch_code']