
from django.urls import path
from . import views

app_name = 'mean_planner'

urlpatterns = [
	#Página Inicial
	path('', views.index, name='index'),
]
