from django.db import models
from django.db.models import CharField, ForeignKey, PositiveIntegerField, BooleanField, ImageField

from users.models import User


# ----------------------------------------------------------------------------------------------------------------------
# Create category model
class Category(models.Model):
    name: CharField = models.CharField(max_length=30)

    class Meta:
        verbose_name: str = "Категория"
        verbose_name_plural: str = "Категории"

        ordering: list[str] = ["name"]

    def __str__(self):
        return self.name


# ----------------------------------------------------------------------------------------------------------------------
# Create advertisement model
class Advertisement(models.Model):
    PUBLISHED: list[tuple] = [
        (True, "Опубликовано"),
        (False, "Не опубликовано")
    ]

    name: CharField = models.CharField(max_length=60)
    author: ForeignKey = models.ForeignKey(User, on_delete=models.CASCADE)
    price: PositiveIntegerField = models.PositiveIntegerField()
    description: CharField = models.CharField(max_length=500)
    is_published: BooleanField = models.BooleanField(choices=PUBLISHED, default=False)
    image: ImageField = models.ImageField(upload_to="images/")
    category: ForeignKey = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name: str = "Объявление"
        verbose_name_plural: str = "Объявления"

        ordering: list[str] = ["-price"]

    def __str__(self):
        return self.name
