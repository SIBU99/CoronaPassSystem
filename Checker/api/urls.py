from django.urls import path
from .views import OnDutyListCreate, OnDutyRetrieveUpdateView, OnDutyLogin, Test

urlpatterns = [
    path("onduty/", OnDutyListCreate.as_view(), name = "OnDuty-list"),
    path("onduty/<int:pk>/", OnDutyRetrieveUpdateView.as_view(), name = "OnDuty-detail"),
    path("login/onduty/", OnDutyLogin.as_view(), name="login-onduty"),
    path("test/", Test.as_view(), name="hopeForSir"),
]
