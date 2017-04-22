#watersourcereport/models.py

from django.db import models

# Create your models here.

WATER_TYPE = (
	('BOT','bottled'),
	('WEL','well'),
	('STR','stream'),
	('LAK','lake'),
	('SPR','spring'),
	('OTH','other'),
)

WATER_CONDITION = (
	('WAS','waste'),
	('TRC','treatable-clear'),
	('TRM','treatable-muddy'),
	('POT','potable'),
)

reportNumber = 0

class WaterSourceReport(models.Model):
	dateTime = models.DateTimeField(auto_now_add=True)
	reportNumber += 1
	reportNum = reportNumber
	reporterName = models.CharField(max_length=300)
	waterLocation = models.CharField(max_length=300)
	waterType = models.CharField(max_length=3, choices=WATER_TYPE)
	waterCondition = models.CharField(max_length=3, choices=WATER_CONDITION)