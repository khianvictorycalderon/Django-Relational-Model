from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RoomViewSet,
    BoarderViewSet,
    OwnerViewSet,
    HouseViewSet,
    PersonViewSet,
    ItemViewSet
)

router = DefaultRouter()

router.register(r'rooms', RoomViewSet)
router.register(r'boarders', BoarderViewSet)
router.register(r'owners', OwnerViewSet)
router.register(r'houses', HouseViewSet)
router.register(r'persons', PersonViewSet)
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]