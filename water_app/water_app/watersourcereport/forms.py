#watersourcereport/forms.py

from django import forms
from .models import WaterSourceReport

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

class WaterSourceReportForm(forms.ModelForm):
	waterType = forms.ChoiceField(choices='WATER_TYPE', required=True)
	waterCondition = forms.ChoiceField(choices='WATER_CONDITION', required=True)

	class Meta:
		model = WaterSourceReport
		fields = ['reporterName', 'waterLocation', 'waterType', 'waterCondition']
