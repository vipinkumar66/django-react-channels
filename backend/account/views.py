from rest_framework import viewsets, status
from rest_framework.response import Response
from models import Account
from rest_framework.permissions import IsAuthenticated
from serializers import RegisterationSerializer

class RegisterationSerializer(viewsets.ModelViewSet):
    """
    We will register user after some basic validations
    Viewset: as it provides much functionality in a one go
    """
    serializer_class = RegisterationSerializer
    def create(self, request, *args, **kwargs):
        """
        we get the serializer from serializer class than give it data
        Than we call is valid method to check whether that data is correct or not
        once it is valid then we call the create method, so it is created after that
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



