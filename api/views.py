from rest_framework import viewsets

from .models import Athlete
from .serializers import AthleteSerializer


class AthleteList(viewsets.ModelViewSet):

    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer
