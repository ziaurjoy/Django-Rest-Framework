from viewsetcreate.models import PersionDetails
from rest_framework import serializers

class PersionDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersionDetails
        fields = "__all__"