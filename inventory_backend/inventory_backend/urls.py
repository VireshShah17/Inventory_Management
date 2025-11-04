"""
URL configuration for inventory_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from party.api import (
    PartyViewSet,
    PersonViewSet,
    PartyGroupViewSet,
    PartyRoleViewSet,
    ContactMechViewSet,
    TelecomNumberViewSet,
    PostalAddressViewSet,
    PartyContactMechViewSet,
)

router = routers.DefaultRouter()
router.register(r'parties', PartyViewSet)
router.register(r'persons', PersonViewSet)
router.register(r'party-groups', PartyGroupViewSet)
router.register(r'party-roles', PartyRoleViewSet)
router.register(r'contacts', ContactMechViewSet)
router.register(r'telecoms', TelecomNumberViewSet)
router.register(r'addresses', PostalAddressViewSet)
router.register(r'party-contactmech', PartyContactMechViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
