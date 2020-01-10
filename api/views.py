from rest_framework import viewsets
from django.shortcuts import redirect

from .serializers import *
from .services import *


def index(request):
    return redirect('/api')


class AthleteView(viewsets.ModelViewSet):

    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer


class AttributesView(viewsets.ModelViewSet):

    queryset = Attributes.objects.all()
    serializer_class = AttributesSerializer


class GamesView(viewsets.ModelViewSet):

    queryset = Games.objects.all()
    serializer_class = GamesSerializer


class TeamView(viewsets.ModelViewSet):

    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class SeasonView(viewsets.ModelViewSet):

    queryset = Season.objects.all()
    serializer_class = SeasonSerializer
    
    
class CityView(viewsets.ModelViewSet):

    queryset = City.objects.all()
    serializer_class = CitySerializer


class SportView(viewsets.ModelViewSet):

    queryset = Sport.objects.all()
    serializer_class = SportSerializer
    

class EventView(viewsets.ModelViewSet):

    queryset = Event.objects.all()
    serializer_class = EventSerializer


class MedalView(viewsets.ModelViewSet):

    queryset = Medal.objects.all()
    serializer_class = MedalSerializer
