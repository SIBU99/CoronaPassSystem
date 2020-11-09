from django.urls import path
from .views import (
    PassApplicationCreate,
    PassApplicationRetrieveUpdateDestroyView,
    PassApplicationList,
    Hope,
    GetFreshData,
    GetStatPlot
)

urlpatterns = [
    path("pass/apply/", PassApplicationCreate.as_view(), name="pass-application"),
    path("pass/check/", PassApplicationList.as_view(), name="pass-check"),
    path("pass/applicant/<slug:pk>/", PassApplicationRetrieveUpdateDestroyView.as_view(), name="pass-applicant"),
    path("send/link/", Hope.as_view(), name="pass-applicant"),
    path("today/stat/", GetFreshData.as_view(), name="today-stat"),
    path("stat/plot/", GetStatPlot.as_view(), name="stat-plot")
]

