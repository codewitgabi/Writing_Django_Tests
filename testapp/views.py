from django.shortcuts import render
from .models import RelatedModel, TestModel

def index(request):
	test_query = request.GET.get("q")
	if test_query is None:
		test_models = TestModel.objects.all()
	else:
		test_query = True if test_query == "active" else False
		test_models = TestModel.objects.filter(active= test_query)
	context = {
		"test_models": test_models,
	}
	return render(request, "index.html", context)