__author__ = 'Miguel'

from sprints.models import Sprint
from user_story.models import UserStory
from django import forms

class SprintModelForm(forms.ModelForm):
	class Meta:
		model = Sprint
		fields = '__all__'

		widgets = {
			'fecha_inicio': forms.DateInput(attrs={'class':'datepicker'}),
			'fecha_fin': forms.DateInput(attrs={'class':'datepicker'}),

		}


