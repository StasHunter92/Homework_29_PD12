from django.db import models
from django.db.models import CharField, DecimalField, PositiveIntegerField, ManyToManyField


# ----------------------------------------------------------------------------------------------------------------------
# Create location model
class Location(models.Model):
    name: CharField = models.CharField(max_length=100)
    lat: DecimalField = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    lng: DecimalField = models.DecimalField(max_digits=9, decimal_places=6, null=True)

    class Meta:
        verbose_name: str = "Локация"
        verbose_name_plural: str = "Локации"
        ordering = ["name"]

    def __str__(self):
        return self.name


# ----------------------------------------------------------------------------------------------------------------------
# Create user model
class User(models.Model):
    ROLES: list[tuple] = [
        ("member", "Участник"),
        ("moderator", "Модератор"),
        ("admin", "Администратор")
    ]

    first_name: CharField = models.CharField(max_length=20)
    last_name: CharField = models.CharField(max_length=20)
    username: CharField = models.CharField(max_length=20)
    password: CharField = models.CharField(max_length=20)
    role: CharField = models.CharField(max_length=20, choices=ROLES, default="member")
    age: PositiveIntegerField = models.PositiveIntegerField()
    locations: ManyToManyField = models.ManyToManyField(Location)

    class Meta:
        verbose_name: str = "Пользователь"
        verbose_name_plural: str = "Пользователи"
        ordering = ["username"]

    def __str__(self):
        return self.username
