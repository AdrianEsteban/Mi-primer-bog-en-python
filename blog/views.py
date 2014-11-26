
# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Entrada

class IndexView(ListView):
	template_name = 'index.html'
	model=Entrada

class Entrada(DetailView):
	template_name = 'entrada_detail.html'
	model=Entrada
	
		

