from django.shortcuts import render
from .models import credit
from .serializers import creditSerializers
from rest_framework.generics import CreateAPIView


class credit_create(CreateAPIView):
    queryset=credit.objects.all()
    serializer_class=creditSerializers