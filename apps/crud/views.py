from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import JsonResponse
from .models import CRUDModel
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic import TemplateView, UpdateView, DeleteView, CreateView, FormView
from django_filters.views import FilterView
from .forms import CRUDForm
from .filters import CRUDFilter

class Index(FilterView):
    template_name = 'index.html'
    model = CRUDModel
    context_object_name = 'models'
    filterset_class = CRUDFilter
    paginate_by = 20

class Create(CreateView):
    template_name = 'create.html'
    form_class = CRUDForm
    success_url = reverse_lazy('crud:index')

    def post(self, request):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'sucess': False, 'errors': form.errors})

class Edit(UpdateView):
    model = CRUDModel
    template_name = 'edit.html'
    form_class = CRUDForm
    success_url = reverse_lazy('crud:create')

class Delete(DeleteView):
    model = CRUDModel
    template_name = 'delete.html'
    success_url = reverse_lazy('crud:create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pk"] = self.kwargs['pk']
        return context