from rest_framework import viewsets, generics
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import redirect
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import *
from .services import *


def index(request):
    return redirect('/api')


class ResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 500


class AthleteView(viewsets.ModelViewSet):

    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'sex']
    pagination_class = ResultsSetPagination


class AthleteFilter(generics.ListAPIView):
    serializer_class = AthleteSerializer

    def get_queryset(self):
        parameters = self.request.query_params.items()
        queryset = Athlete.objects.all()

        filters = []

        for key, value in parameters:
            filter = ".filter({}__name='{}')".format(key, value)
            filters.append(filter)

        queryset = eval("queryset{}".format("".join(filters)))
        return queryset


class AttributesView(viewsets.ModelViewSet):

    queryset = Attributes.objects.all()
    serializer_class = AttributesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['age', 'height', 'weight', 'year']


class GamesView(viewsets.ModelViewSet):

    queryset = Games.objects.all()
    serializer_class = GamesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']


class TeamView(viewsets.ModelViewSet):

    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']


class SeasonView(viewsets.ModelViewSet):

    queryset = Season.objects.all()
    serializer_class = SeasonSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']
    
    
class CityView(viewsets.ModelViewSet):

    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']


class SportView(viewsets.ModelViewSet):

    queryset = Sport.objects.all()
    serializer_class = SportSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']
    

class EventView(viewsets.ModelViewSet):

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']


class MedalView(viewsets.ModelViewSet):

    queryset = Medal.objects.all()
    serializer_class = MedalSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']
