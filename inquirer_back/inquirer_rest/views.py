from django.shortcuts import render
from rest_framework import generics
from inquirer_rest.models import Inquirer
from inquirer_rest.serializers import InquirerSerializer
# Create your views here.


class InquirerAPIView(generics.ListAPIView):
    queryset = Inquirer.objects.all()
    serializer_class = InquirerSerializer
