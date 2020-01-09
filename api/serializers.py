from rest_framework import serializers
from .models import Athlete, Attributes


class AthleteSerializer(serializers.ModelSerializer):
    # attributes = AttributesSerializer(many=True, read_only=True)
    class Meta:

        model = Athlete
        fields = ["name", "sex"]


class AttributesSerializer(serializers.ModelSerializer):
    athlete = AthleteSerializer(read_only=True)
    class Meta:

        model = Attributes
        fields = ["year", "age", "height", "weight", "athlete"]

