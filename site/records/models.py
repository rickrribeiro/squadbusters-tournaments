from django.db import models
from tournament.models import Player
class RecordType(models.Model):
    ORDER_TYPES = [
            ("biggest", "Maior"),
            ("lowest", "Menor")
    ]
    name = models.CharField(max_length=100)
    unity = models.CharField(max_length=50, null=True, blank=True)
    order_type = models.CharField(max_length=50, choices=ORDER_TYPES, default="biggest")
    
    def __str__(self):
        return self.name

class Record(models.Model):
    record_type = models.ForeignKey(RecordType, on_delete=models.CASCADE)
    date = models.DateField()
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    value = models.FloatField()
    
    def __str__(self):
        return f"Record of {self.record_type.name}"
