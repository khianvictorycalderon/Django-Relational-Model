from rest_framework import serializers
from .models import Room, Boarder, Owner, House, Person, Item

# ------------------------------------------------------------
# One-to-Many Relationship
# Room -> many Boarders

class BoarderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boarder
        fields = ['id', 'name', 'room']


class RoomSerializer(serializers.ModelSerializer):
    boarders = BoarderSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ['id', 'number', 'boarders']


# ------------------------------------------------------------
# One-to-One Relationship
# Owner -> one House

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ['id', 'number', 'owner']


class OwnerSerializer(serializers.ModelSerializer):
    house = HouseSerializer(read_only=True)

    class Meta:
        model = Owner
        fields = ['id', 'name', 'house']


# ------------------------------------------------------------
# Many-to-Many Relationship
# Person <-> Item

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'name']


class ItemSerializer(serializers.ModelSerializer):
    buyer = PersonSerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = ['id', 'name', 'buyer']