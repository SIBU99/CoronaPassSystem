from rest_framework.generics import(
ListCreateAPIView,
#RetrieveUpdateDestroyAPIView,
RetrieveUpdateAPIView,
#CreateAPIView,
#ListAPIView,
#RetrieveAPIView,
#UpdateAPIView,
#DestroyAPIView,
)
import requests as req
from django.contrib.auth import authenticate
from rest_framework.permissions import(
    #AllowAny,
    IsAuthenticated,
    #IsAdminUser,
    #IsAuthenticatedOrReadOnly,
    #DjangoModelPermissions,
    #DjangoModelPermissionsOrAnonReadOnly,
    #DjangoObjectPermissions
)
from ..models import OnDuty
from .serializers import OnDutySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class OnDutyListCreate(ListCreateAPIView):
    queryset = OnDuty.objects.all()
    serializer_class = OnDutySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        "this will filter the backeng as per requirement"
        queryset = OnDuty.objects.all()
        params = dict()
        if self.request.query_params.get("dist", None):
            params["district"] = self.request.query_params.get("dist")
        if self.request.query_params.get("block", None):
            params["block"] = self.request.query_params.get("block")
        if self.request.query_params.get("workstation", None):
            params["workstation"] = self.request.query_params.get("workstation")
        if self.request.query_params.get("fullname", None):
            params["fullname"] = self.request.query_params.get("fullname")
        
        if len(params):
            queryset = OnDuty.objects.all().filter(**params)
        return queryset

class OnDutyRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = OnDuty.objects.all()
    serializer_class = OnDutySerializer
    permission_classes = [IsAuthenticated]

class OnDutyLogin(APIView):
    def post(self, request, format=None):
        "this will run ever the post is called"
        username = request.data.get("username")
        password = request.data.get("password")

        payload = {
            "username":username,
            "password":password
        }

        url = "https://covid19odishapass.herokuapp.com/api/v1/token/"

        r = req.post(url, data=payload)
        if r.status_code == 200:
            data = r.json()
            user = authenticate(username = username,password = password)
            onduty = user.UserOnDuty
            serializer = OnDutySerializer(onduty)
            data = {**data,**serializer.data}
            return Response(data, status = status.HTTP_200_OK)
        else:
            msg = {
                "Error": "Enter The Correct Username and password"
            }
            return Response(msg, status= status.HTTP_404_NOT_FOUND)
            


class Test(APIView):
        "this will read the querystring"
        def post(self, request, format=None):
            username = request.query_params.get("username")
            password = request.query_params.get("password")
            payload = {
                "username":username,
                "password":password
            }
            return Response(payload, status= status.HTTP_404_NOT_FOUND)





