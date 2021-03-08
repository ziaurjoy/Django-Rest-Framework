

from ClassBasedAPI.models import Persion
from rest_framework import serializers

class PersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persion
        fields = "__all__"

