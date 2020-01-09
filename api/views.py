from rest_framework import viewsets

from .models import Athlete
from .serializers import *
from .services import *

download_csv_file_from_kaggle()
# insert_data()


class AthleteList(viewsets.ModelViewSet):

    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer


class AttributesList(viewsets.ModelViewSet):

    queryset = Attributes.objects.all()
    serializer_class = AttributesSerializer


class GamesList(viewsets.ModelViewSet):

    queryset = Games.objects.all()
    serializer_class = GamesSerializer


class MedalList(viewsets.ModelViewSet):

    queryset = Medal.objects.all()
    serializer_class = MedalSerializer