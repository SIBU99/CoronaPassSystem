from rest_framework import serializers 
from ..models import CheckUpRequest

class CheckUpRequestSerializer(serializers.ModelSerializer):
   "This the serializer for the model : CheckUpRequest"
   class Meta:
        model = CheckUpRequest
        fields = "__all__"