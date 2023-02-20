from rest_framework import serializers
from rest_framework.fields import IntegerField, CharField
from rest_framework.relations import SlugRelatedField

from users.models import Location, User


# ----------------------------------------------------------------------------------------------------------------------
# Location serializers
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model: Location = Location
        fields: str = "__all__"


# ----------------------------------------------------------------------------------------------------------------------
# User serializers
class UserListSerializer(serializers.ModelSerializer):
    """
    Serializer for ListView
    """
    locations: SlugRelatedField = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )

    class Meta:
        model: User = User
        exclude: list[str] = ["password"]


class UserDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for DetailView
    """
    locations: SlugRelatedField = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )

    class Meta:
        model: User = User
        exclude: list[str] = ["id"]


class UserCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for CreateView
    """
    id: IntegerField = serializers.IntegerField(required=False)
    locations: SlugRelatedField = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Location.objects.all(),
        slug_field="name"
    )

    class Meta:
        model: User = User
        fields: str = "__all__"

    def is_valid(self, raise_exception=False) -> bool:
        """
        Validate data

        :return: bool
        """
        self._locations = self.initial_data.pop("locations")
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        """
        Create user from validated data
        """
        user = User.objects.create(**validated_data)

        for location in self._locations:
            location_obj, _ = Location.objects.get_or_create(name=location)
            user.locations.add(location_obj)
        user.save()

        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for UpdateView
    """
    locations: SlugRelatedField = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Location.objects.all(),
        slug_field="name"
    )
    role: CharField = serializers.CharField(read_only=True)
    id: IntegerField = serializers.IntegerField(read_only=True)

    class Meta:
        model: User = User
        fields: str = "__all__"

    def is_valid(self, raise_exception=False) -> bool:
        """
        Validate data

        :return: bool
        """
        self._locations = self.initial_data.pop("locations")
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        """
        Save locations to User
        """
        user = super().save()

        for location in self._locations:
            location_obj, _ = Location.objects.get_or_create(name=location)
            user.locations.add(location_obj)
        user.save()

        return user


class UserDeleteSerializer(serializers.ModelSerializer):
    """
    Serializer for DeleteView
    """

    class Meta:
        model: User = User
        fields: list[str] = ["id"]
