from django.shortcuts import render
from .serializers import phoneSerializers
from .models import phone
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter



class phoneView(ListAPIView):
    queryset=phone.objects.all()
    serializer_class=phoneSerializers
    filter_backends=[SearchFilter]
    search_fields=['^mobile']