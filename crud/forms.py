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



class MiFormulario(forms.Form):
    opciones_operacion = [
        ('opcion1', 'Opción 1'),
        ('opcion2', 'Opción 2'),
        ('opcion3', 'Opción 3'),
    ]
     
    clave_pedimento = forms.CharField(
        max_length=100,
        label="Clave de pedimento",
        widget=forms.TextInput(attrs={'placeholder': 'Clave pedimento'})
    )
    tipo_operacion = forms.ChoiceField(
        choices=opciones_operacion,
        widget=forms.Select(),
        label="Tipo de operación"
    )
    fecha_inicio = forms.DateField(
        label="Fecha inicio",
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    fecha_fin = forms.DateField(
        label="Fecha fin",
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    descripcion = forms.CharField(
        label="Descripción",
        widget=forms.Textarea(attrs={'placeholder': 'Descripción'})
    )
    estado = forms.ChoiceField(
        choices=opciones_operacion,
        widget=forms.Select(),
        label="Estado"
    )

   
