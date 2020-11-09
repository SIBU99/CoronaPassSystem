from django.urls import path 
from .views import (
    PersonRetrieveUpdateDestroyView,
    PersonList,
)

urlpatterns = [
    path("persons/", PersonList.as_view(), name = "Person-List"),
    path("persons/<slug:pk>/", PersonRetrieveUpdateDestroyView.as_view(), name="Person-detail"),
]

