import django_filters
from django import forms
from .models import CRUDModel

class CRUDFilter(django_filters.FilterSet):
    class Meta:
        model = CRUDModel
        fields = [
            'int',
        ]

    def __init__(self, *args, **kwargs):
        super(CRUDFilter, self).__init__(*args, **kwargs)

        self.filters['int'].label = 'Entero'
        self.filters['int'].field.widget.attrs.update({
            'placeholder': 'Entero',
            'class': 'form-control'
        })