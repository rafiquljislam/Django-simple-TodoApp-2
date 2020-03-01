from django import forms
from django.forms import ModelForm

from .models import Todos

class TodosForm(forms.ModelForm):
    class Meta:
        model = Todos
        fields = "__all__"