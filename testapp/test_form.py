from django.test import TestCase, Client
from .models import TestModel
from django.urls import reverse


class PostRequest(TestCase):
	def test_active_form(self):
		data = {"name": "TestForm", "active": True}
		response = self.client.post("/create/", data= data)
		self.assertEqual(response.status_code, 302)
		
	def test_inactive_form(self):
		data = {"name": "TestForm", "active": False}
		response = self.client.post("/create/", data= data)
		self.assertEqual(response.status_code, 302)
		
	def test_invalid_fieldname(self):
		data = {"names": "TestForm", "active": False}
		response = self.client.post("/create/", data= data)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.templates[0].name, "form.html")
		
		
class PutRequest(TestCase):
	def test_update(self):
		mod = TestModel.objects.create(name= "tester")
		data = {"name": "TestForm", "active": True}
		response = self.client.post(f"/update/{mod.id}", data= data)
		
		self.assertEqual(response.status_code, 302)
		