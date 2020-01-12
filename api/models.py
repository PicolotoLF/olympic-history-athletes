from django.db import models


class Games(models.Model):

    class Meta:
        db_table = 'games'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True, null=False)


class Team(models.Model):

    class Meta:
        db_table = 'team'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True, null=False)


class Season(models.Model):
    class Meta:
        db_table = 'season'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, unique=True)


class City(models.Model):
    class Meta:
        db_table = 'city'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, unique=True)


class Sport(models.Model):
    class Meta:
        db_table = 'sport'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, unique=True)


class Event(models.Model):
    class Meta:
        db_table = 'event'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, unique=True)


class Medal(models.Model):
    class Meta:
        db_table = 'medal'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, unique=True)


class Attributes(models.Model):
    """This it's another table because if an athlete have more than one participation, attributes like
    Age, Height and Wight may vary over the years."""

    class Meta:
        db_table = 'attributes'

    age = models.IntegerField(null=False)
    height = models.DecimalField(max_digits=15, decimal_places=2, null=False)
    weight = models.DecimalField(max_digits=15, decimal_places=2, null=False)
    year = models.IntegerField(null=False)


class Athlete(models.Model):
    class Meta:
        db_table = 'athlete'

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, null=False)
    sex = models.CharField(max_length=10, null=False)

    games = models.ForeignKey(Games, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    medal = models.ForeignKey(Medal, on_delete=models.CASCADE)
    attributes = models.ForeignKey(Attributes, on_delete=models.CASCADE)



