from rest_framework import serializers
from .models import *


class AttributesSerializer(serializers.ModelSerializer):
    class Meta:

        model = Attributes
        fields = ["year", "age", "height", "weight"]


class GamesSerializer(serializers.ModelSerializer):
    # attributes = AttributesSerializer(many=True, read_only=True)
    class Meta:

        model = Games
        fields = ["name"]


class MedalSerializer(serializers.ModelSerializer):
    # attributes = AttributesSerializer(many=True, read_only=True)
    class Meta:

        model = Medal
        fields = ["name"]


class AthleteSerializer(serializers.ModelSerializer):
    attributes = AttributesSerializer(read_only=True)
    games = GamesSerializer(read_only=True)
    class Meta:

        model = Athlete
        fields = ["name", "sex", "attributes", "games"]