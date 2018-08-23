# coding=utf-8
from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate, logout
from .models import *
from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.template.context_processors import request
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib import messages
from .forms import *

def cria_cliente(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conta Criada com sussesso!')
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'cadastro/index.html', {'form': form})

def apresentacao(request):
    return render(request, 'index.html')

@require_POST
def entrar(request):
    usuario_aux = User.objects.get(email=request.POST['email'])
    usuario = authenticate(username=usuario_aux.username,
                           password=request.POST["senha"])
    if usuario is not None:
        login(request, usuario)
        return HttpResponseRedirect('/home/')

    return HttpResponseRedirect('/')

@login_required
def sair(request):
    logout(request)
    return HttpResponseRedirect('/')

def sala_show(request):
    return render(request, 'sala_apresentacao.html')


def sala_receive(request):
    return render(request, 'sala_recebe.html')


def criaanuncio(request):
    if request.method == 'POST':
        form  = FormClienteAnuncio(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit = False)
            item.cliente = request.user
            item.save()
    else:
        form = FormClienteAnuncio()
    return render(request, 'cadastro/index.html', {'form':form})

def cam_girls(request):
    template_name = 'cam-girls.html'
    girls_list = ClienteAnuncio.objects.all()
    return render(request, template_name, {'girls_list' : girls_list, 't_girls_list': len(girls_list)} )
    
def girls_profile(request, nr_item):
    try:
        item = ClienteAnuncio.objects.get(pk = nr_item)
    except:
        raise Http404('/')
    return render(request, "girls_profiles/item_girls.html", {'item': item})

def acompanhantes(request):
    template_name = 'acompanhantes.html'
    acompanhantes_list = {'Joana' 'Carla' 'Sua mae'}
    return render(request, template_name, {'acompanhantes_list': acompanhantes_list})

def motels(request):
    motel_list = Motel.objects.all()
    for motel in motel_list:
        print motel.nome
    template_name = 'motels.html'
    return render(request, template_name, {'motel_list': motel_list})

def motel_profile(request, motel_id):
    motel = Motel.objects.get(
        id=motel_id,
    )
    print motel
    template_name = 'motel-profile.html'
    return render(request, template_name, {'motel': motel})
