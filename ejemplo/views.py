import time
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.generic import FormView

from .forms import MiFormulario, FormularioLoading

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

class CreateLoading(FormView):
    template_name = 'ejemplo/create_loading.html'
    form_class = FormularioLoading

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            # Puse un sleep para fines de mostrar el alert con el elemento de loading
            time.sleep(5)
            messages.success(request,'El registro se realizó con éxito.')
            return redirect(reverse_lazy('ejemplo:index'))
        messages.error(request,'No se pudo realizar el registro.')
        return render(request, self.template_name, context={'form':form})