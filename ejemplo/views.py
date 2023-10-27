from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import MiFormulario


def index(request):
    return render(request, "ejemplo/index.html") 

def indexitem(request):
    return render(request, "ejemplo/indexitem.html")

class Create(FormView):
    template_name = 'ejemplo/create.html'
    form_class = MiFormulario
