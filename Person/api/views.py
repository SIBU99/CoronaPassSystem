from rest_framework.generics import(
#ListCreateAPIView,
RetrieveUpdateDestroyAPIView,
#RetrieveUpdateAPIView,
#CreateAPIView,
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
from ..models import Person
from .serialisers import PersonSerializer

class PersonList(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        "this will filter the backeng as per requirement"
        queryset = Person.objects.all()
        params = dict()
        if self.request.query_params.get("district", None):
            params["district"] = self.request.query_params.get("district")
        if self.request.query_params.get("workstation", None):
            params["workstation"] = self.request.query_params.get("workstation")
        if self.request.query_params.get("lastName", None):
            params["lastName"] = self.request.query_params.get("lastName")
        
        if len(params):
            queryset = Person.objects.all().filter(**params)
        return queryset

class PersonRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [AllowAny]


