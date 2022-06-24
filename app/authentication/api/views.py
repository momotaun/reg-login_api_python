from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from ..models import User
from .serializers import RegisterUserSerializer
from rest_framework import(
    generics,
    status,
    views
    )


class RegisterAPIView(generics.GenericAPIView):
    
    serializer_class = RegisterUserSerializer
    
    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)