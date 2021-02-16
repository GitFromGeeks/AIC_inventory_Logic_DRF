from django.shortcuts import render
from .serializers import stockinfoSerializers
from rest_framework.generics import ListAPIView
from .models import stockinfo



class stockinfoView(ListAPIView):
    queryset=stockinfo.objects.all()
    serializer_class=stockinfoSerializers