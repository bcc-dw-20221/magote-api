"""Adicionando itens na interface admin do django."""
from django.contrib import admin

from .models import CornoProfile

# Register your models here.
admin.site.register(CornoProfile)