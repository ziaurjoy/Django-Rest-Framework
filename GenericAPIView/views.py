from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework import mixins
from GenericAPIView.models import Admission
from GenericAPIView.serializer import AdmissionSerializer



from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.


# GenericAPIView

"""class AdmissionAllApi(generics.GenericAPIView, 
mixins.CreateModelMixin, 
mixins.ListModelMixin, 
mixins.RetrieveModelMixin,
mixins.UpdateModelMixin,
mixins.DestroyModelMixin): 
 
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer
    lookup_field = 'id'

    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id)
        else:
            return self.list(request)
    def post(self, request):
        return self.create(request)
    def put(self, request, id):
        return self.update(request, id)
    def delete(self, request, id):
        return self.destroy(request, id)"""




# GenericViewSet

"""class AdmissionAllApi(viewsets.GenericViewSet, 
mixins.CreateModelMixin, 
mixins.ListModelMixin, 
mixins.RetrieveModelMixin,
mixins.UpdateModelMixin,
mixins.DestroyModelMixin): 
 
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer"""


# ModelViewSet
class AdmissionAllApi(viewsets.ModelViewSet): 
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer



