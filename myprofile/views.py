from django.shortcuts import render
from .serializers import myprofileSerializers
from rest_framework.generics import ListAPIView
from .models import myprofile



class myprofileView(ListAPIView):
    queryset=myprofile.objects.all()
    serializer_class=myprofileSerializers