from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet

from users.models import Location, User
from users.serializers import LocationSerializer, UserListSerializer, UserDetailSerializer, UserCreateSerializer, \
    UserUpdateSerializer, UserDeleteSerializer


# ----------------------------------------------------------------------------------------------------------------------
# Location ViewSet
class LocationsViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


# ----------------------------------------------------------------------------------------------------------------------
# User ApiView
class UserListView(ListAPIView):
    """
    GET list of users
    """
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserDetailView(RetrieveAPIView):
    """
    GET one user
    """
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class UserCreateView(CreateAPIView):
    """
    POST to create user
    """
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserUpdateView(UpdateAPIView):
    """
    PATCH to update user
    """
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer


class UserDeleteView(DestroyAPIView):
    """
    DELETE to delete user
    """
    queryset = User.objects.all()
    serializer_class = UserDeleteSerializer
