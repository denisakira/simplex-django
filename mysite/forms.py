from django import forms
from django.forms import formset_factory
from .models import Simplex, Oferta, Demanda

class SimplexForm(forms.ModelForm):
    class Meta:
        model = Simplex
        fields = "__all__"

class OfertaForm(forms.ModelForm):
    class Meta:
        model = Oferta
        fields = "__all__"

class DemandaForm(forms.ModelForm):
    class Meta:
        model = Demanda
        fields = "__all__"

class NumberForm(forms.Form):
    lista = ((0,0),(1,1),(2,2),(3,3),(4,4),(5,5))
    Oferta = forms.ChoiceField(choices=lista)
    Demanda = forms.ChoiceField(choices=lista)
