from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . views import  UserLoginApiView,  UserLogoutAPIView, UserAccountCreateSerializer, UserAddressCreateSerializer

# router = DefaultRouter()
# router.register("login", UserLoginApiView, basename="login")
# router.register("register", UserRegistrationApiView, basename="register")
# router.register("logout", UserRegistrationApiView, basename="logout")



urlpatterns = [
    # path("", include(router.urls)),
    # path("", UserRegistrationApiView.as_view(), name = 'registration'),
    path("", UserAccountCreateSerializer.as_view(), name = 'account' ),
    path("login/", UserLoginApiView.as_view(), name = 'login'),
    path("logout/", UserLogoutAPIView.as_view(), name = 'logout'),

  

]
