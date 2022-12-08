from django import forms
from .models import TestModel

class TestModelForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		
		self.fields["name"].widget.attrs.update({
			"type": "text",
			"id": "name",
			"name": "name",
			"required": "",
			"placeholder": "Name"
		})
		self.fields["active"].widget.attrs.update({
			"type": "checkbox",
			"name": "active",
			"id": "active"
		})
	class Meta:
		model = TestModel
		fields = ["name", "active"]