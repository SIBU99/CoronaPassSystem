from rest_framework import serializers 
from ..models import Person

class PersonSerializer(serializers.ModelSerializer):
   "This the serializer for the model : Person"
   class Meta:
        model = Person
        fields = "__all__"