from django.shortcuts import render
from django.urls import reverse_lazy
from .models import CRUDModel
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic import TemplateView, UpdateView, DeleteView, CreateView, FormView
from .forms import CRUDForm, MiFormulario

class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['models'] = CRUDModel.objects.all()
        return context

class Create(FormView):
    template_name = 'create.html'
    form_class = MiFormulario
    success_url = reverse_lazy('crud:index')



class Edit(UpdateView):
    model = CRUDModel
    template_name = 'create.html'
    form_class = MiFormulario
    success_url = reverse_lazy('crud:index')

    def post(self, request, pk): 
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        #form = CRUDForm(request.POST)
        errors = form.errors
        char = form
        raise KeyError