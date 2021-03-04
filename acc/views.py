from django.shortcuts import render
from .serializers import accSerializers
from .models import accessorie
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter



class accView(ListAPIView):
    queryset=accessorie.objects.all()
    serializer_class=accSerializers
    filter_backends=[SearchFilter]
    search_fields=['^acc_name']