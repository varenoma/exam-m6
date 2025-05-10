from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from qatagon.models import QatagonClass

# Create your views here.


class ListViewQatagon(ListView):
    model = QatagonClass
    template_name = 'base.html'
    context_object_name = 'qatagon'
    paginate_by = 10


class DetailViewQatagon(DetailView):
    model = QatagonClass
    template_name = 'qatagon/detail.html'
    context_object_name = 'detail'


class UpdateViewQatagon(UpdateView):
    model = QatagonClass
    fields = ['full_name', 'birth_date', 'died_date',
              'description', 'region', 'ayblov']
    template_name = 'qatagon/update.html'
    context_object_name = 'update'
    success_url = reverse_lazy('qatagon:home')


class DeleteViewQatagon(DeleteView):
    model = QatagonClass
    template_name = 'qatagon/delete.html'
    context_object_name = 'delete'
    success_url = reverse_lazy('qatagon:home')
