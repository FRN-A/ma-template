from django import forms
import datetime
from .models import CRUDModel

class CRUDForm(forms.ModelForm):
    class Meta:
        model = CRUDModel
        fields = [
            'int',
            'char',
            'text',
            'date',
        ]

        labels = {
            'int': 'Entero',
            'char': 'Alfanumérico',
            'text':'Texto',
            'date':'Fecha',
        }

        widgets = {
            'int': forms.NumberInput(attrs={'placeholder': 'Entero', 'class': 'form-control'}),
            'char': forms.TextInput(attrs={'placeholder': 'Alfanumérico', 'class': 'form-control'}),
            'text': forms.Textarea(attrs={'placeholder': 'Texto'}),
            'date': forms.DateInput(attrs={'type': 'date'}),
        }




   
