from django import forms
from .models import Simplex

class SimplexForm(forms.ModelForm):
    class Meta:
        model = Simplex
        fields = "__all__"
