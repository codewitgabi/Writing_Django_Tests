from django.shortcuts import render, redirect
from .models import RelatedModel, TestModel
from .forms import TestModelForm
from django.views.decorators.csrf import csrf_exempt


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
	

@csrf_exempt	
def create_model(request):
	form = TestModelForm()
	if request.method == "POST":
		form = TestModelForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("index")
	return render(request, "form.html", {"form": form})
	
	
def update_model(request, id):
	instance = TestModel.objects.get(id= id)
	form = TestModelForm(request.POST or None, instance= instance)
	if form.is_valid():
		form.save()
		return redirect("index")
	return render(request, "form.html", {"form": form})