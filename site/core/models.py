from django.db import models

# Create your models here.


class Clan(models.Model):
	name = models.CharField(max_length=100)
	logo = models.ImageField(upload_to="clan_logos/", blank=True, null=True)

	def __str__(self):
		return self.name


class Player(models.Model):
	nick = models.CharField(max_length=50)
	clan = models.ForeignKey(Clan, on_delete=models.SET_NULL, null=True, blank=True)
	player_id = models.CharField(max_length=50, primary_key=True)

	def __str__(self):
		return self.nick