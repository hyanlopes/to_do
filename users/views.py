from rest_framework import generics
from rest_framework.authentication import TokenAuthentication

from .models import User
from .permissions import IsAdminPermission
from .serializers import UserSerializer


class UserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserListView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminPermission]
    serializer_class = UserSerializer
    queryset = User.objects.all()


# Create your views here.
