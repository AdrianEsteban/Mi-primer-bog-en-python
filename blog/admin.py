from django.contrib import admin
from .models import Entrada
from django_markdown.admin import MarkdownModelAdmin

admin.site.register(Entrada)
class EntradaAdmin(MarkdownModelAdmin):
	pass
		
