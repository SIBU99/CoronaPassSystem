from django.urls import path
from .views import (
    AuthorizerListCreate,
    AuthorizerRetrieveUpdateView,
    AuthorizerLogin,
)

urlpatterns = [
    path("authorizer/", AuthorizerListCreate.as_view(), name="authorizer"),
    path("authorizer/<slug:pk>/", AuthorizerRetrieveUpdateView.as_view(), name="authorizer-deatial"),
     path("login/authorizer/", AuthorizerLogin.as_view(), name="login-authorizer"),
]
