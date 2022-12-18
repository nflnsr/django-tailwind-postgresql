from django.forms import ModelForm
from .models import Todolist

class TodolistForm(ModelForm):
    class Meta:
        model = Todolist
        fields = '__all__'