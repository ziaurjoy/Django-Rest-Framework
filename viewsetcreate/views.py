from django.shortcuts import render
from rest_framework import viewsets
from viewsetcreate.models import PersionDetails
from viewsetcreate.serializer import PersionDetailsSerializer
# Create your views here.


class PersionDetailsViewSet(viewsets.ModelViewSet):
    queryset = PersionDetails.objects.all()
    serializer_class = PersionDetailsSerializer
    
