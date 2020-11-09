from rest_framework import serializers
from ..models import Authorizer
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):
   "This the serializer for the model : User"
   class Meta:
        model = User
        fields = [
           "id",
           "username",
           "password",
        ]
        extra_kwargs = {
           "password":{
              "write_only":True
           }
        }

class AuthorizerSerializer(serializers.ModelSerializer):
   "This the serializer for the model : Authorizer"
   auth = UserSerializer()
   class Meta:
        model = Authorizer
        fields = "__all__"
   
   def create(self, validated_data):
      "This will create the instance for many to many field "
      auth = validated_data.pop("auth")
      username = auth.pop("username")
      password = auth.pop("password")
      try:
         user = User.objects.create(
            username = username,
         )
         user.set_password(password)
         user.save()
      except:
         msg = {
           "Error":"Please Provide a Valid Useraname and Password"
         }
         raise ValidationError(msg)

      try:
         authorizer = Authorizer.objects.create(
            **validated_data,
            auth = user,        
         )
      except:
         msg = {
           "Error":"Failed to create a Authorizer"
         }
         raise ValidationError(msg)

      return authorizer


class AuthorizerHelpSerializer(serializers.ModelSerializer):
    "This the serializer for the model : Authorizer"
    class Meta:
         model = Authorizer
         fields = [
           "district",
           "block",
           "fullname",
           "designation",
           "workstation"
         ]
         read_only_fields = [
           "district",
           "block",
           "fullname",
           "designation",
           "workstation"
        ]