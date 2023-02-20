from django.db.models import Q
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet

from ads.models import Category, Advertisement
from ads.serializers import CategorySerializer, AdvertisementListSerializer, AdvertisementDetailSerializer, \
    AdvertisementCreateSerializer, AdvertisementUpdateSerializer, AdvertisementDeleteSerializer


# ----------------------------------------------------------------------------------------------------------------------
# Category ViewSet
class CategoriesViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# ----------------------------------------------------------------------------------------------------------------------
# Advertisement ApiView
class AdvertisementListView(ListAPIView):
    """
    GET list of advertisements
    """
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementListSerializer

    def get(self, request, *args, **kwargs):
        """
        Filter results
        """
        categories = request.GET.getlist("cat", None)
        categories_q = None

        for category in categories:
            if categories_q is None:
                categories_q = Q(category__name__icontains=category)
            else:
                categories_q |= Q(category__name__icontains=category)

        if categories_q:
            self.queryset = self.queryset.filter(categories_q)

        advertisement_text = request.GET.get("text", None)

        if advertisement_text:
            self.queryset = self.queryset.filter(name__icontains=advertisement_text)

        location = request.GET.get("loc", None)

        if location:
            self.queryset = self.queryset.filter(author__locations__name__icontains=location)

        price_from = request.GET.get("price_from", None)

        if price_from:
            self.queryset = self.queryset.filter(price__gt=price_from)

        price_to = request.GET.get("price_to", None)

        if price_to:
            self.queryset = self.queryset.filter(price__lt=price_to)

        return super().get(request, *args, **kwargs)


class AdvertisementDetailView(RetrieveAPIView):
    """
    GET one advertisement
    """
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementDetailSerializer


class AdvertisementCreateView(CreateAPIView):
    """
    POST to create advertisement
    """
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementCreateSerializer


class AdvertisementUpdateView(UpdateAPIView):
    """
    PATCH to update advertisement
    """
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementUpdateSerializer


class AdvertisementDeleteView(DestroyAPIView):
    """
    DELETE to delete advertisement
    """
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementDeleteSerializer


@method_decorator(csrf_exempt, name="dispatch")
class AdUploadImage(UpdateView):
    model: Advertisement = Advertisement
    fields: list[dict] = ["name", "price", "description", "author", "category"]

    def post(self, request, *args, **kwargs) -> JsonResponse:
        """
        Handle a POST request to the AdvertisementView. Creates a new image object in the database

        :param request: The incoming request object
        :return: A JSON response with a dictionary representing the updated Ad object
        """
        self.object = self.get_object()

        try:
            self.object.image = request.FILES.get("image")
            self.object.save()
        except Exception:
            return JsonResponse({"error": "Wrong data"}, status=400)

        response: dict = {
            "id": self.object.id,
            "name": self.object.name,
            "description": self.object.description,
            "author_id": self.object.author_id,
            "author": self.object.author.username,
            "is_published": self.object.is_published,
            "category_id": self.object.category_id,
            "category": self.object.category.name,
            "image": self.object.image.url if self.object.image else None
        }

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False}, status=200)
