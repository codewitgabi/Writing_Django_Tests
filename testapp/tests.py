from django.test import TestCase, Client
from .models import TestModel, RelatedModel


class MyTest(TestCase):
	""" Testing for model methods """
	def setUp(self):
		TestModel.objects.create(name= "test1", active= True)
		TestModel.objects.create(name= "test2")
		
	def test_is_active(self):
		obj = TestModel.objects.get(name= "test1")
		self.assertEqual(obj.is_active, "test1 is active")
		
	def test_not_active(self):
		obj = TestModel.objects.get(name= "test2")
		self.assertEqual(obj.is_active, "not active")
		

class ViewTest(TestCase):
	""" Test a view """
	def test_index_view(self):
		client = Client()
		response = client.get("/")
		#print(response.templates[0].source)
		self.assertEqual(response.status_code, 200)
		
		""" Test that the correct template was rendered """
		self.assertTrue(response.templates[0].name == "index.html")
		
