from django.db import models

# Django has 3 types of relationship, one-to-many, many-to-many, and one-to-one

# --------------------------------------------------------------------
# One to Many Relationship (One room can have multiple boarder)
class Room(models.Model):
    number = models.PositiveIntegerField()

class Boarder(models.Model):
    name = models.CharField(max_length=255)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="boarders")

# --------------------------------------------------------------------
# One to One Relationship (Only one owner per house)
class Owner(models.Model):
    name = models.CharField(max_length=255)

class House(models.Model):
    number = models.PositiveIntegerField()
    owner = models.OneToOneField(Owner, on_delete=models.CASCADE, related_name="house")
# --------------------------------------------------------------------
# Many to Many Relationship (Many people can have many items)
class Person(models.Model):
    name = models.CharField(max_length=255)

class Item(models.Model):
    name = models.CharField(max_length=100)
    buyer = models.ManyToManyField(Person, related_name="items")
# --------------------------------------------------------------------