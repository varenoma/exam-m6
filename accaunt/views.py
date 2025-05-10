from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CustomUserForm

# Create your views here.


class HomePage(LoginRequiredMixin, TemplateView):
    template_name = 'accaunt/accaunt_home.html'

    login_url = 'accaunt:signup'


class SignUpView(FormView):
    template_name = 'accaunt/signup.html'
    form_class = CustomUserForm
    success_url = reverse_lazy('qatagon:home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


def logout_def(request):
    logout(request)
    return redirect(reverse_lazy('accaunt:signup'))
