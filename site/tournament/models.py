from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from core.models import Clan, Player


class Tournament(models.Model):
	TOURNAMENT_TYPES = [
		("LBSB", "LBSB"),
		("SQUADCUP", "Squad Cup"),
		("TREINO_CLAS", "5x5 de clãs"),
	]
	name = models.CharField(max_length=100)
	table_header_name = models.CharField(max_length=100, null=True, blank=True)
	tournament_type =  models.CharField(max_length=20, choices=TOURNAMENT_TYPES)
	clan1 = models.ForeignKey(Clan, on_delete=models.CASCADE, related_name="clan1_tournaments", null=True, blank=True)
	clan2 = models.ForeignKey(Clan, on_delete=models.CASCADE, related_name="clan2_tournaments", null=True, blank=True)
	date = models.DateField()
	pointsFormat = models.ForeignKey("PointsFormat", on_delete=models.SET_NULL, null=True, blank=True)
	isFinished = models.BooleanField(default=False)
 
	def __str__(self):
		return self.name


class TournamentMatch(models.Model):
	tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
	date = models.DateField()

	def __str__(self):
		return f"Match of {self.tournament.name} on {self.date}"


class PlayerMatch(models.Model):
	tournament_match = models.ForeignKey(TournamentMatch, on_delete=models.CASCADE)
	player = models.ForeignKey(Player, on_delete=models.CASCADE)
	gems = models.PositiveIntegerField(default=0)
	killed_by = models.ForeignKey(
		Player,
		related_name="killed_players",
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
	)
	clan = models.ForeignKey(
		Clan, on_delete=models.SET_NULL, null=True, blank=True
	)
	position = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(1)])

	def save(self, *args, **kwargs):
		if not self.clan and self.player.clan:
			self.clan = self.player.clan
		super().save(*args, **kwargs)

	def __str__(self):
		return f"Match data for {self.player.nick}"


class PointsFormat(models.Model):
	name = models.CharField(max_length=50)
	points1 = models.IntegerField(default=0)
	points2 = models.IntegerField(default=0)
	points3 = models.IntegerField(default=0)
	points4 = models.IntegerField(default=0)
	points5 = models.IntegerField(default=0)
	points6 = models.IntegerField(default=0)
	points7 = models.IntegerField(default=0)
	points8 = models.IntegerField(default=0)
	points9 = models.IntegerField(default=0)
	points10 = models.IntegerField(default=0)
	points_per_kill = models.IntegerField(default=0)
	lost_points_per_death = models.IntegerField(default=0, validators=[MaxValueValidator(0)])

	def __str__(self):
		return self.name
