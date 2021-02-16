from django.shortcuts import render
from .serializers import phoneSerializers
from rest_framework.generics import ListAPIView
from .models import phone


class phoneView(ListAPIView):
    queryset=phone.objects.all()
    serializer_class=phoneSerializers