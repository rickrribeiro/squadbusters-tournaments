from django.db import models
from tournament.models import Player
class RecordType(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Record(models.Model):
    record_type = models.ForeignKey(RecordType, on_delete=models.CASCADE)
    date = models.DateField()
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    value = models.IntegerField()
    
    def __str__(self):
        return f"Record of {self.record_type.name}"
