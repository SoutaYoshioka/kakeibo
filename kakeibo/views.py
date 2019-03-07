from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Category, Kakeibo
from .forms import KakeiboForm
from django.urls import reverse_lazy


class KakeiboListView(ListView):

    model = Kakeibo


class KakeiboCreateView(CreateView):

    model = Kakeibo
    form_class = KakeiboForm
    success_url = reverse_lazy('kakeibo:create_done')


def create_done(request):

    return render(request, 'kakeibo/create_done.html')


class KakeiboUpdateView(UpdateView):

    model = Kakeibo
    form_class = KakeiboForm
    success_url = reverse_lazy('kakeibo:update_done')


def update_done(request):

    return render(request, 'kakeibo/update_done.html')
