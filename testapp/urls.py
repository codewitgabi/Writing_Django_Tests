from django.urls import path
from .views import *


urlpatterns = [
	path("", index, name= "index"),
	path("create/", create_model, name= "create"),
	path("update/<int:id>", update_model, name= "update"),
]