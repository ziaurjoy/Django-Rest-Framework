

from GenericAPIView.models import Admission
from rest_framework import serializers

class AdmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admission
        fields = "__all__"