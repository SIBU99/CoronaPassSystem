from django.urls import path
from .views import (
    CheckUpRequestCreate,
    CheckUpRequestList,
    CheckUpReuestListRetrieveUpdateView,
)

urlpatterns = [
    path("medicalcheckup/", CheckUpRequestCreate.as_view(), name="checkup-create"),
    path("medicalcheckup/list/", CheckUpRequestList.as_view(), name="checkup-list"),
    path("medicalcheckup/<int:pk>/", CheckUpReuestListRetrieveUpdateView.as_view(), name="checkup-detail")
]
