from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url as r

from .forms import FakeModelForm
from .models import Fake


def home(request):
    if request.method == 'POST':
        busca = search(request)

        form = FakeModelForm(request.POST)

        if form.is_valid() and not counter(request):
            form.save()
            messages.success(request, 'Cadastrado com sucesso')
            return HttpResponseRedirect(r('core:home'))
        else:
            messages.success(request, 'Já foi registrado 5 possiveis fakenews')

    else:
        busca = lista_fakes()
        form = FakeModelForm()
    return render(request, 'core/index.html', {'busca': busca, 'form': form})


def lista_fakes():
    return Fake.objects.all()


def counter(request):
    ur = request.POST.get('url')
    url = Fake.objects.filter(url=ur)
    if url.count() >= 5:
        return True


def search(request):
    url_buscada = request.POST.get('url_buscada')
    if url_buscada:
        url = Fake.objects.filter(
            Q(url=url_buscada),
            Q(url__contains=url_buscada))

        if not url:
            messages.success(request, 'Valor nao existe')
            url = lista_fakes()
        return url

