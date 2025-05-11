from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from qatagon.models import QatagonClass

# Create your views here.


class ListViewQatagon(ListView):
    model = QatagonClass
    template_name = 'base.html'
    context_object_name = 'qatagon'


class DetailViewQatagon(DetailView):
    model = QatagonClass
    template_name = 'qatagon/detail.html'
    context_object_name = 'detail'


class UpdateViewQatagon(LoginRequiredMixin, UpdateView):
    model = QatagonClass
    fields = ['full_name', 'birth_date', 'died_date',
              'description', 'region', 'ayblov']
    template_name = 'qatagon/update.html'
    context_object_name = 'update'
    success_url = reverse_lazy('qatagon:home')

    login_url = 'accaunt:signup'


class DeleteViewQatagon(LoginRequiredMixin, DeleteView):
    model = QatagonClass
    template_name = 'qatagon/delete.html'
    context_object_name = 'delete'
    success_url = reverse_lazy('qatagon:home')

    login_url = 'accaunt:signup'


def search_view(request):
    query = request.GET.get('q', '')
    results = []

    if query:
        results = QatagonClass.objects.filter(full_name__icontains=query)

    return render(request, 'qatagon/search.html', {
        'results': results,
        'query': query,
    })
