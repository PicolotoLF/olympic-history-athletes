from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from .models import *


class AttributesSerializer(serializers.ModelSerializer):
    class Meta:

        model = Attributes
        fields = "__all__"


class GamesSerializer(serializers.ModelSerializer):
    class Meta:

        model = Games
        fields = "__all__"


class TeamSerializer(serializers.ModelSerializer):
    class Meta:

        model = Team
        fields = "__all__"


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:

        model = Season
        fields = "__all__"


class CitySerializer(serializers.ModelSerializer):
    class Meta:

        model = City
        fields = "__all__"


class SportSerializer(serializers.ModelSerializer):
    class Meta:

        model = Sport
        fields = "__all__"


class EventSerializer(serializers.ModelSerializer):
    class Meta:

        model = Event
        fields = "__all__"


class MedalSerializer(serializers.ModelSerializer):
    class Meta:

        model = Medal
        fields = "__all__"


class AthleteFilterSerializer(serializers.ModelSerializer):
    class Meta:

        model = Athlete
        fields = "__all__"


class AthleteSerializer(WritableNestedModelSerializer):
    attributes = AttributesSerializer()
    games = GamesSerializer()
    team = TeamSerializer()
    season = SeasonSerializer()
    city = CitySerializer()
    sport = SportSerializer()
    event = EventSerializer()
    medal = MedalSerializer()

    class Meta:
        model = Athlete
        fields = ["id", "name", "sex", "attributes", "games", "team",
                  "season", "city", "sport", "event", "medal"]