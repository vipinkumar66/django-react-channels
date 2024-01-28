from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.exceptions import MethodNotAllowed
from .serializers import RegisterationSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from django.conf import settings

class RegisterationViewset(viewsets.ModelViewSet):
    """
    We will register user after some basic validations
    Viewset: as it provides much functionality in a one go
    It should have the queryset or it should overwrite the getqueryset method
    otherwise it will thow the assertion error this is due to the model view set
    """
    serializer_class = RegisterationSerializer

    def get(self, request, *args, **kwargs):
        raise MethodNotAllowed("GET method is not allowed for registration.")

    def put(self, request, *args, **kwargs):
        raise MethodNotAllowed("PUT method is not allowed for registration.")

    def patch(self, request, *args, **kwargs):
        raise MethodNotAllowed("PATCH method is not allowed for registration.")

    def delete(self, request, *args, **kwargs):
        raise MethodNotAllowed("DELETE method is not allowed for registration.")

    def get_queryset(self):
        return None

    def create(self, request, *args, **kwargs):
        """
        we get the serializer from serializer class than give it data
        Than we call is valid method to check whether that data is correct or not
        once it is valid then we call the create method, so it is created after that
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response({"message":f"Account created for {user.username}"},
                        status=status.HTTP_201_CREATED, headers=headers)

class JWTSetCookieMixin:
    def finalize_response(self, request, response, *args, **kwargs):
        if response.data.get("access"):
            response.set_cookie(
                settings.SIMPLE_JWT["ACCESS_TOKEN_NAME"], response.data["access"],
                max_age = settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"],
                httponly = True,
                samesite = settings.SIMPLE_JWT["JWT_COOKIE_SAMESITE"]
            )
        if response.data.get("refresh"):
            response.set_cookie(
                settings.SIMPLE_JWT["REFRESH_TOKEN_NAME"], response.data["refresh"],
                max_age = settings.SIMPLE_JWT["REFRESH_TOKEN_LIFETIME"],
                httponly = True,
                samesite = settings.SIMPLE_JWT["JWT_COOKIE_SAMESITE"]
            )
        # del response.data["access"]
        # del response.data["refresh"]
        return super().finalize_response(request, response, *args, **kwargs)


class JWTCookieTokenObtainPairView(JWTSetCookieMixin, TokenObtainPairView):
    pass



