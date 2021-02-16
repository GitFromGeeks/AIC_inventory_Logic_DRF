from django.shortcuts import render
from .models import inventory
from  .serializers import inventorySerializers
from rest_framework.generics import ListCreateAPIView

from django.http import HttpResponse


class inventoryView(ListCreateAPIView):
    queryset=inventory.objects.filter(branch_code='AIC06AH')
    serializer_class=inventorySerializers