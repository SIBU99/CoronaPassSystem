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
from rest_framework.permissions import(
    AllowAny,
    IsAuthenticated,
    #IsAdminUser,
    #IsAuthenticatedOrReadOnly,
    #DjangoModelPermissions,
    #DjangoModelPermissionsOrAnonReadOnly,
    #DjangoObjectPermissions
)
from ..models import Authorizer
from Authority.api.serializers import AuthorizerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests as req
from django.contrib.auth import authenticate


class AuthorizerListCreate(ListCreateAPIView):
    queryset = Authorizer.objects.all()
    serializer_class = AuthorizerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        "this will filter the backeng as per requirement"
        queryset = Authorizer.objects.all()
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
            queryset = Authorizer.objects.all().filter(**params)
        return queryset

class AuthorizerRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = Authorizer.objects.all()
    serializer_class = AuthorizerSerializer
    permission_classes = [IsAuthenticated]

class AuthorizerLogin(APIView):
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
            authorizer = user.UserAuthority
            serializer = AuthorizerSerializer(authorizer)
            data = {**data,**serializer.data}
            return Response(data, status = status.HTTP_201_CREATED)
        else:
            msg = {
                "Error": "Enter The Correct Username and password"
            }
            return Response(msg, status= status.HTTP_404_NOT_FOUND)