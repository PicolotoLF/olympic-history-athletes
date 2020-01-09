from django.db import models


class Attributes(models.Model):
    """This it's another table because if an athlete have more than one participation, attributes like
    Age, Height and Wight may vary over the years."""

    class Meta:
        db_table = 'attributes'

    id = models.IntegerField(primary_key=True)
    age = models.IntegerField(null=True)
    height = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    weight = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    year = models.IntegerField(null=True)


class Games(models.Model):

    class Meta:
        db_table = 'games'

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)


class Team(models.Model):

    class Meta:
        db_table = 'team'

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    noc = models.CharField(max_length=15)


class Season(models.Model):
    class Meta:
        db_table = 'season'

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, null=True)


class City(models.Model):
    class Meta:
        db_table = 'city'

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, null=True)


class Sport(models.Model):
    class Meta:
        db_table = 'sport'

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, null=True)


class Event(models.Model):
    class Meta:
        db_table = 'event'

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, null=True)


class Medal(models.Model):
    class Meta:
        db_table = 'medal'

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, null=True)


class Athlete(models.Model):
    class Meta:
        db_table = 'athlete'

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    sex = models.CharField(max_length=10)

    attributes = models.ForeignKey(Attributes, on_delete=models.CASCADE)
    games = models.ForeignKey(Games, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    medal = models.ForeignKey(Medal, on_delete=models.CASCADE)
