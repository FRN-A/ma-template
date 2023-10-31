from django import forms

class MiFormulario(forms.Form):
    opciones = [
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
        choices=opciones,
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

    # Select 2
    estado = forms.ChoiceField(
        choices=opciones,
        widget=forms.Select(attrs={"data-control": "select2", "data-placeholder": "Elige un estado"}),
        label="Estado"
    )

    checkbox = forms.BooleanField(required=False)

    radio = forms.ChoiceField(
        widget= forms.RadioSelect(),
        choices=opciones, 
    )

class FormularioLoading(forms.Form):
    elemento1 = forms.CharField(max_length=255, label="Elemento 1", widget=forms.TextInput(attrs={'placeholder':'Elemento 1'}))