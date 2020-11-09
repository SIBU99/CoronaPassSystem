from rest_framework import serializers 
from ..models import PassApplication
from rest_framework.exceptions import ValidationError
from Authority.models import Authorizer
from Authority.api.serializers import AuthorizerHelpSerializer
from pprint import pprint
class PassApplicationSerializer(serializers.ModelSerializer):
   "This the serializer for the model : PassApplication"
   requestedAuthority = AuthorizerHelpSerializer(required=False)
   class Meta:
        model = PassApplication
        fields = "__all__"
   
   def create(self, validated_data):
      "This will create the instance for many to many field " 
      pprint(validated_data)
      dist = validated_data.pop("district")
      workstation = validated_data.pop("workstation")
      authorizer = Authorizer.objects.get(district=dist, workstation=workstation)
      fastFill = validated_data.pop("fastFill", None)
      data = None
      
      if fastFill:
         AadharCardFUrl = validated_data.pop("AadharCardFUrl")
         AadharCardBUrl = validated_data.pop("AadharCardBUrl")
         recentPictureUrl = validated_data.pop("recentPictureUrl")

         try:
            data = PassApplication.objects.create(
               **validated_data,
               district=dist,
               workstation=workstation,
               requestedAuthority = authorizer,
               AadharCardFUrl = AadharCardFUrl,
               AadharCardBUrl = AadharCardBUrl,
               recentPictureUrl = recentPictureUrl
            )
         except:
            msg = "PLease Provide a Valid Pass Application 1"
            raise ValidationError(msg)
      else:
         AadharCardF = validated_data.pop("AadharCardF")
         AadharCardB = validated_data.pop("AadharCardB")
         recentPicture = validated_data.pop("recentPicture")
         #try:
         data = PassApplication.objects.create(
               **validated_data,
               district=dist,
               workstation=workstation,
               requestedAuthority = authorizer,
               AadharCardF = AadharCardF,
               AadharCardB = AadharCardB,
               recentPicture = recentPicture
            )
         # except:
         #    msg = "PLease Provide a Valid Pass Application 2"
         #    raise ValidationError(msg)
         
      return data

