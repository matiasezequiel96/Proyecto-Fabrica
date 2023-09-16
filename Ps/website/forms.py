from django import forms
from .models import Record

class AddRecordForm(forms.ModelForm):
    nombre_pieza = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Nombre", "class":"form-control"}), label="")
    material = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Material", "class":"form-control"}), label="")
    numero_molde = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Matriz", "class":"form-control"}), label="")

    class Meta:
        model = Record
        exclude = ("user",)