from rest_framework import serializers
from rest_framework.fields import SerializerMethodField, IntegerField, ImageField
from rest_framework.relations import SlugRelatedField

from ads.models import Category, Advertisement


# ----------------------------------------------------------------------------------------------------------------------
# Category serializers
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model: Category = Category
        fields: str = "__all__"


# ----------------------------------------------------------------------------------------------------------------------
# Advertisement serializers
class AdvertisementListSerializer(serializers.ModelSerializer):
    """
    Serializer for ListView
    """
    author: SlugRelatedField = serializers.SlugRelatedField(read_only=True, slug_field="first_name")
    category: SlugRelatedField = serializers.SlugRelatedField(read_only=True, slug_field="name")

    class Meta:
        model: Advertisement = Advertisement
        exclude: list[str] = ["is_published"]


class AdvertisementDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for DetailView
    """
    author: SlugRelatedField = serializers.SlugRelatedField(read_only=True, slug_field="first_name")
    category: SlugRelatedField = serializers.SlugRelatedField(read_only=True, slug_field="name")
    locations: SerializerMethodField = SerializerMethodField()

    def get_locations(self, advertisement) -> list:
        """
        Make list of locations

        :param advertisement: Object of advertisement
        :return: List of locations
        """
        return [location.name for location in advertisement.author.locations.all()]

    class Meta:
        model: Advertisement = Advertisement
        fields: list[str] = ['name', 'author', 'price', 'description', 'is_published', 'image', 'category', 'locations']


class AdvertisementCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for CreateView
    """
    id: IntegerField = serializers.IntegerField(required=False)
    image: ImageField = serializers.ImageField(required=False)

    class Meta:
        model: Advertisement = Advertisement
        fields: str = "__all__"


class AdvertisementUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for UpdateView
    """
    id: IntegerField = serializers.IntegerField(read_only=True)

    class Meta:
        model: Advertisement = Advertisement
        fields: str = "__all__"


class AdvertisementDeleteSerializer(serializers.ModelSerializer):
    """
    Serializer for DeleteView
    """

    class Meta:
        model: Advertisement = Advertisement
        fields: list[str] = ["id"]
