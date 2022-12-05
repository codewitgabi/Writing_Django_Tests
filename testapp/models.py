from django.db import models


class TestModel(models.Model):
	name = models.CharField(max_length= 200)
	date_created = models.DateTimeField(auto_now_add= True)
	active = models.BooleanField(default= False)
	
	def __str__(self):
		return self.name
		
	@property
	def is_active(self):
		return f"{self.name} is active" if self.active == True else f"not active"
		
		
class RelatedModel(models.Model):
	name = models.CharField(max_length= 200)
	test_model = models.ForeignKey(TestModel, on_delete= models.CASCADE)
	date_created = models.DateTimeField(auto_now_add= True)
	
	def __str__(self):
		return self.name