from django.shortcuts import render
from ClassBasedAPI.models import Persion
from ClassBasedAPI.serializer import PersionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.renderers import TemplateHTMLRenderer
# Create your views here.


class PersionList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'
    def get(self, request, format=None):
        persions = Persion.objects.all()
        persions_serializer = PersionSerializer(persions,many = True)
        return Response({'persions': persions})

class PersionCreate(APIView):
    def post(self, request, format=None):
        persions_serializer = PersionSerializer(data=request.data)
        if persions_serializer.is_valid():
            persions_serializer.save()
            return Response(persions_serializer.data, status=status.HTTP_201_CREATED)
        return Response(persions_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PersionUpdate(APIView):
    
    def get_persion(self, id):
        try:
            return Persion.objects.get(id=id)
        except Persion.DoesNotExist:
            Response(Persion.errors,status=status.HTTP_404_NOT_FOUND)
        
   
         

    def get(self, request, id, format=None):
        persion = self.get_persion(id)
        persion_serializer = PersionSerializer(persion)
        return Response(persion_serializer.data)

    def put(self, request, id, format=None):
        persion = self.get_persion(id)
        persion_serializer = PersionSerializer(persion, data=request.data)
        if persion_serializer.is_valid():
            persion_serializer.save()
            return Response(persion_serializer.data)
        return Response(persion_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        persion = self.get_persion(id)
        persion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    

    

