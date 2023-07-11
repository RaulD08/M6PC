from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import Permission, User
from django.contrib.contenttypes.models import ContentType
from django import forms
from .models import VehiculoModel
from .forms import *



# Create your views here.


def index(request):

    admin = User.objects.get(id=1)
    context = {
        'user_has_perm': request.user.has_perm('vehiculo.visualizar_catalogo'),
        'user_has_perm_2': request.user.has_perm('vehiculo.add_vehiculomodels'),
        'admin': admin,
    }
    return render(request, 'index.html', context)
   

def vehiculo_add(request):

    if request.user.has_perm('vehiculo.add_vehiculomodels'):
        form = VehiculoForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            form.save()
            messages.success(request, "Vehículo agregado correctamente.")
            return HttpResponseRedirect('/vehiculo/add')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error en el campo '{form.fields[field].label}': {error}")
        
        admin = User.objects.get(id=1)
        context = {
            'form': form,
            'user_has_perm': request.user.has_perm('vehiculo.visualizar_catalogo'),
            'user_has_perm_2': request.user.has_perm('vehiculo.add_vehiculomodels'),
            'admin': admin,
        }
        return render(request, 'vehiculo_add.html', context)
    elif request.user.is_authenticated == False:
        messages.warning(request, "Por favor, inicie sesión para ingresar al portal.")
        return HttpResponseRedirect('/login')
    else:
        return HttpResponseRedirect('/403')


def registro_view(request):

    if request.user.is_authenticated == False:
        if request.method == "POST":
            form = RegistroUsuarioForm(request.POST)
            if form.is_valid():
                # obtenemos el content type del modelo
                content_type = ContentType.objects.get_for_model(VehiculoModel)
                # obtenemos el permiso a asignar
                visualizar_catalogo = Permission.objects.get(codename='visualizar_catalogo', content_type=content_type)
                user = form.save()
                # Agregamos el permiso al usuario el momento de registrarse
                user.user_permissions.add(visualizar_catalogo)
                login(request, user)
                messages.success(request, "Registrado Satisfactoriamente.")
                return HttpResponseRedirect ('/')
        
            messages.error(request, "Registro invalido. Algunos datos son incorrectos.")
        form = RegistroUsuarioForm()
        admin = User.objects.get(id=1)
        return render (request= request, template_name="register.html", context={"register_form":form, 'admin': admin})
    else:
        messages.info(request, "Ya ha iniciado sesión.")
        return HttpResponseRedirect('/')


def login_view(request):

    if request.user.is_authenticated == False:
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.info (request, f"Iniciaste sesión como: {username}")
                    return HttpResponseRedirect('/')
                else:
                    messages.error(request, "Usuario o contraseña inválido.")
            else:
                messages.error(request, "Usuario o contraseña inválido.")
        
        form = AuthenticationForm()
        admin = User.objects.get(id=1)
        context = {
            'login_form' : form,
            'admin': admin
        }
        return render(request, "login.html", context)
    else:
        messages.info(request, "Ya ha iniciado sesión.")
        return HttpResponseRedirect('/')


def logout_view(request):
    logout(request)
    messages.success(request, "Se ha cerrado la sesión satisfactoriamente.")
    return HttpResponseRedirect('/')


def vehiculo_list(request):
        
    if request.user.has_perm('vehiculo.visualizar_catalogo'):
        datos = VehiculoModel.objects.all()  
        
        admin = User.objects.get(id=1)
        context = {
            'datos': datos,
            'user_has_perm': request.user.has_perm('vehiculo.visualizar_catalogo'),
            'user_has_perm_2': request.user.has_perm('vehiculo.add_vehiculomodels'),
            'admin': admin
        }
        return render(request, 'vehiculo_list.html', context)
    elif request.user.is_authenticated == False:
        messages.warning(request, "Por favor, inicie sesión para ingresar al portal.")
        return HttpResponseRedirect('/login')
    else:
        return HttpResponseRedirect('/403')


def no_permiso(request):
    
    admin = User.objects.get(id=1)
    context = {
            'user_has_perm': request.user.has_perm('vehiculo.visualizar_catalogo'),
            'user_has_perm_2': request.user.has_perm('vehiculo.add_vehiculomodels'),
            'admin': admin
    }
    return render(request, '403.html', context)