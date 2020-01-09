from django.db import models


class Athlete(models.Model):
    class Meta:
        db_table = 'athlete'

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    sex = models.CharField(max_length=10)

    def __str__(self):
        return self.name


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

    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)


class Games(models.Model):

    class Meta:
        db_table = 'games'

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)


class Team(models.Model):

    class Meta:
        db_table = 'team'

    athlete = models.OneToOneField(
        Athlete,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    name = models.CharField(max_length=255)
    noc = models.CharField(max_length=15)


class Season(models.Model):
    class Meta:
        db_table = 'season'

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, null=True)

    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)


class City(models.Model):
    class Meta:
        db_table = 'city'

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, null=True)

    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)


class Sport(models.Model):
    class Meta:
        db_table = 'sport'

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, null=True)

    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)


class Event(models.Model):
    class Meta:
        db_table = 'event'

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, null=True)

    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)


class Medal(models.Model):
    class Meta:
        db_table = 'medal'

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, null=True)

    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)