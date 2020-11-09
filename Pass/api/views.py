from rest_framework.generics import(
#ListCreateAPIView,
RetrieveUpdateDestroyAPIView,
#RetrieveUpdateAPIView,
CreateAPIView,
ListAPIView,
#RetrieveAPIView,
#UpdateAPIView,
#DestroyAPIView,
)
from rest_framework.permissions import(
    AllowAny,
    IsAuthenticated,
    #IsAdminUser,
    IsAuthenticatedOrReadOnly,
    #DjangoModelPermissions,
    #DjangoModelPermissionsOrAnonReadOnly,
    #DjangoObjectPermissions
)
from rest_framework.parsers import (
    #JSONParser,
    FormParser,
    MultiPartParser,
    #FileUploadParser,
)
from ..models import PassApplication
from .serialisers import PassApplicationSerializer
import requests as req
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import send_the_link
from django.utils import timezone
from django.db.models import Count
from rest_framework.filters import(
SearchFilter,
OrderingFilter
)

class PassApplicationList(ListAPIView):
    queryset = PassApplication.objects.all()
    serializer_class = PassApplicationSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = [
        "$firstName", 
        "$lastName", 
        "=phoneNumber", 
        "=email", 
        "=AadharCardNo"
    ]
    ordering_fields = ['startTime']
    ordering = ['startTime']

    
    def get_queryset(self):
        "this will filter the backeng as per requirement"
        queryset = PassApplication.objects.all()
        params = dict()
        if self.request.query_params.get("id", None):
            params["requestedAuthority__id"] = self.request.query_params.get("id")
        if self.request.query_params.get("status", None):
            params["status"] = self.request.query_params.get("status")
        if self.request.query_params.get("day", None):
            params["startTime__day"] = self.request.query_params.get("day")
        if self.request.query_params.get("month", None):
            params["startTime__month"] = self.request.query_params.get("month")
        if self.request.query_params.get("year", None):
            params["startTime__year"] = self.request.query_params.get("year")
        if self.request.query_params.get("srday", None):
            params["startTime__day__gte"] = self.request.query_params.get("srday")
        if self.request.query_params.get("srmonth", None):
            params["startTime__month__gte"] = self.request.query_params.get("srmonth")
        if self.request.query_params.get("sryear", None):
            params["startTime__year__gte"] = self.request.query_params.get("sryear")
        if self.request.query_params.get("erday", None):
            params["startTime__day__lte"] = self.request.query_params.get("erday")
        if self.request.query_params.get("ermonth", None):
            params["startTime__month__lte"] = self.request.query_params.get("ermonth")
        if self.request.query_params.get("district", None):
            params["district"] = self.request.query_params.get("district")
        if self.request.query_params.get("block", None):
            params["block"] = self.request.query_params.get("block")
        
        
        if len(params):
            queryset = PassApplication.objects.all().filter(**params)
        return queryset
    
class PassApplicationCreate(CreateAPIView):
    queryset = PassApplication.objects.all()
    serializer_class = PassApplicationSerializer
    permission_classes = [AllowAny]
    parser_classes = (
        FormParser,
        MultiPartParser,
    )


class PassApplicationRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = PassApplication.objects.all()
    serializer_class = PassApplicationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class Hope(APIView):
    def get(self, request, format=None):
            name = self.request.data.get("name")
            phone = self.request.data.get("phone")
            aadhar = self.request.data.get("aadhar")
            url = f"http://kumarashirwradmishra.pythonanywhere.com/send/{name}/{phone}/{aadhar}"
            r = req.get(url=url)
            return Response({"status":r.status_code, "data":r.json()}, status= status.HTTP_404_NOT_FOUND)


class GetFreshData(APIView):
    "this will generate the live count of all the data"
    def get(self, request, format=None):
        "this will help to get the fresh data count"

        today = timezone.now()
        dataDay = self.request.query_params.get("day", None)
        dataMonth = self.request.query_params.get("month", None)
        dataYear = self.request.query_params.get("year", None)
        filter_set = {
            "startTime__day": dataDay if dataDay else today.day,
            "startTime__month":dataMonth if dataMonth else today.month,
            "startTime__year":dataYear if dataYear else today.year,
            # "district":self.request.query_params.get("district", None),
            # "block":self.request.query_params.get("block", None),
            # "requestedAuthority__id": self.request.query_params.get("id", None)
        }
        if self.request.query_params.get("district", None):
           filter_set["district"] =  self.request.query_params.get("district")
        if self.request.query_params.get("block", None):
           filter_set["block"] =  self.request.query_params.get("block")
        if self.request.query_params.get("id", None):
           filter_set["requestedAuthority__id"] =  self.request.query_params.get("id")

        p = PassApplication.objects.all().filter(**filter_set).values("status").annotate(count = Count("status"))
        pl = list(p)
        #final = [] #this will hold the inforation
        final = { i["status"]:i["count"] for i in pl }
        final["Not"] = final.get("Not", 0)
        final["Reject"] = final.get("Reject", 0)
        final["Held"] = final.get("Held", 0)
        final["Approve"] = final.get("Approve", 0)
        final["Total"] = sum(final.values())


        return Response(final, status=status.HTTP_200_OK)

class GetStatPlot(APIView):
    def get(self, request, format =None):
        "this wil return the Points of date"
        filterSet = dict() #empty filter set
        
        if self.request.query_params.get("id", None):
            filterSet["requestedAuthority__id"] = self.request.query_params.get("id")
        if self.request.query_params.get("srday", None):
            filterSet["startTime__day__gte"] = self.request.query_params.get("srday")
        if self.request.query_params.get("srmonth", None):
            filterSet["startTime__month__gte"] = self.request.query_params.get("srmonth")
        if self.request.query_params.get("sryear", None):
            filterSet["startTime__year__gte"] = self.request.query_params.get("sryear")
        if self.request.query_params.get("erday", None):
            filterSet["startTime__day__lte"] = self.request.query_params.get("erday")
        if self.request.query_params.get("ermonth", None):
            filterSet["startTime__month__lte"] = self.request.query_params.get("ermonth")
        if self.request.query_params.get("district", None):
            filterSet["district"] = self.request.query_params.get("district")
        if self.request.query_params.get("block", None):
            filterSet["block"] = self.request.query_params.get("block")
        
        
        
        dic = dict() #emptyfinalset
        p = PassApplication.objects.all().filter(**filterSet).values("status", "startTime__date").annotate(count = Count("status"))

        p = list(p)
        for i in p:
            i["startTime__date"] = i["startTime__date"].strftime("%d-%b-%y")
        for i in p:
            if dic.get(i["startTime__date"], None):
                dic[i["startTime__date"]] = {**dic[i["startTime__date"]], **{i["status"]:i["count"]}}
            else:
                dic[i["startTime__date"]] = {i["status"]:i["count"]}
        
        compare = {"Approve", "Not", "Reject", "Held", "Held"}
        for i, j in zip(dic.values(), dic.keys()):  
            a = list(compare - set(list(i.keys())))
            for k in a:                             
                dic[j] = {**dic[j], **{k:0}}
        
        return Response(dic, status=status.HTTP_200_OK)



