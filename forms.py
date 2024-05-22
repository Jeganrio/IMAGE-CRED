# forms.py
from django import forms
from image_app.models import Hotel
class HotelForm(forms.ModelForm):
	class Meta:
		model = Hotel
		fields = "__all__"
