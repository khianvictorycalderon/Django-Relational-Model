from rest_framework import viewsets
from .models import Room, Boarder, Owner, House, Person, Item
from .serializers import (
    RoomSerializer,
    BoarderSerializer,
    OwnerSerializer,
    HouseSerializer,
    PersonSerializer,
    ItemSerializer
)

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class BoarderViewSet(viewsets.ModelViewSet):
    queryset = Boarder.objects.all()
    serializer_class = BoarderSerializer


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer