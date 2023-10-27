from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.generic import FormView
from .forms import MiFormulario


def index(request):
    return render(request, "ejemplo/index.html") 

def indexitem(request):
    return render(request, "ejemplo/indexitem.html")

class Create(FormView):
    template_name = 'ejemplo/create.html'
    form_class = MiFormulario

    def post(self, request):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        
        if form.is_valid():
            
            return JsonResponse({'data': form.data})
        else:
            return JsonResponse({'sucess': False, 'errors': form.errors})
