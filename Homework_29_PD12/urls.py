"""Homework_29_PD12 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from Homework_29_PD12 import settings
from ads.views import CategoriesViewSet
from users.views import LocationsViewSet

# ----------------------------------------------------------------------------------------------------------------------
# Create router
router = routers.SimpleRouter()

# ----------------------------------------------------------------------------------------------------------------------
# Register routes
router.register('location', LocationsViewSet)
router.register('category', CategoriesViewSet)

# ----------------------------------------------------------------------------------------------------------------------
# Register urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('users.urls')),
    path('ad/', include('ads.urls')),
]
urlpatterns += router.urls

# ----------------------------------------------------------------------------------------------------------------------
# Debug for image
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
