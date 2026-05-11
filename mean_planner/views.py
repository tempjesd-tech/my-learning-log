from django.shortcuts import render

# Create your views here.

def index(request):
	"""A página inicial de Learning Log"""
	return render(request, 'mean_planner/index.html')
