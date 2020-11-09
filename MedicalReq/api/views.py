from rest_framework.generics import(
#ListCreateAPIView,
#RetrieveUpdateDestroyAPIView,
RetrieveUpdateAPIView,
CreateAPIView,
ListAPIView,
#RetrieveAPIView,
#UpdateAPIView,
#DestroyAPIView,
)
from rest_framework.permissions import(
    AllowAny,
    #IsAuthenticated,
    #IsAdminUser,
    #IsAuthenticatedOrReadOnly,
    #DjangoModelPermissions,
    #DjangoModelPermissionsOrAnonReadOnly,
    #DjangoObjectPermissions
)
from ..models import CheckUpRequest
from .serializers import CheckUpRequestSerializer


class CheckUpRequestCreate(CreateAPIView):
    queryset = CheckUpRequest.objects.all()
    serializer_class = CheckUpRequestSerializer
    permission_classes = [AllowAny]

class CheckUpRequestList(ListAPIView):
    queryset = CheckUpRequest.objects.all()
    serializer_class = CheckUpRequestSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        "this will filter the backeng as per requirement"
        queryset = CheckUpRequest.objects.all()
        params = dict()
        if self.request.query_params.get("status", None):
            params["status"] = self.request.query_params.get("status")
        if self.request.query_params.get("day", None):
            params["when__day"] = self.request.query_params.get("day")
        if self.request.query_params.get("month", None):
            params["when__month"] = self.request.query_params.get("month")
        if self.request.query_params.get("year", None):
            params["when__year"] = self.request.query_params.get("year")
        
        if len(params):
            queryset = CheckUpRequest.objects.all().filter(**params).order_by("-when")
        return queryset

class CheckUpReuestListRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = CheckUpRequest.objects.all()
    serializer_class = CheckUpRequestSerializer
    #permission_classes = []