from rest_framework import serializers
from ..models import OnDuty
from Authority.api.serializers import UserSerializer
from django.contrib.auth.models import User

from rest_framework.exceptions import ValidationError

class OnDutySerializer(serializers.ModelSerializer):
    "This the serializer for the model : OnDuty"
    auth = UserSerializer()
    class Meta:
        model = OnDuty
        fields = [
            "id",
            "auth",
            "fullname",
            "designation",
            "workstation",
            "district",
            "block",
            "checkedToday",
            "phoneNumber",
            "email", 
        ]

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
            onduty = OnDuty.objects.create(
                **validated_data,
                auth = user,        
            )
        except:
            msg = {
                "Error":"Failed to create a Authorizer"
            }
            raise ValidationError(msg)

        return onduty