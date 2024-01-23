'''from django.shortcuts import render

#======================
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

#======================


def casa(request):
    return render(request, 'index.html')

def perfil(request):
    return render(request, 'perfil.html')

def registro_user(request):
    return render(request, 'registro_user.html')




#logout =============

def custom_logout(request):
    logout(request)
    return redirect('/index')

#logout =============


def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index.html') 

    return render(request, 'login.html')



'''

from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.conf import settings


class Home(LoginRequiredMixin, View):
    template_name = 'libreria/index.html'
    login_url = 'login'

    def get(self, request):
        return render(request, self.template_name)



def registro_user(request):
    return render(request, 'registro_user.html')

def index(request):
    return render(request, 'index.html')

def perfil(request):
    return render(request, 'perfil.html')

def garage(request):
    return render(request, 'garage.html')

def venta_auto(request):
    return render(request, 'venta_auto.html')

def contacto(request):
    return render(request, 'contacto.html')

# mapa



def mapa_view(request):
    context = {
        'GOOGLE_MAPS_API_KEY': settings.GOOGLE_MAPS_API_KEY
    }
    return render(request, 'myapp/mapa.html', context)


# -----------------------------------------------
#logout =============

def custom_logout(request):
    logout(request)
    return redirect('index')

#logout =============


def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index.html')

    return render(request, 'login.html')

# ----------------------------------------------------------------





# LOGIN 

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

'''def login_view(request):
    error_message = None

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('perfil.html')  # Redireciona para a página de perfil após o login
        else:
            error_message = 'Credenciais inválidas. Por favor, tente novamente.'

    return render(request, 'login.html', {'error_message': error_message})

def logout_view(request):
    logout(request)
    return redirect('index.html')  # Redireciona para a página principal após o logout

'''


# REGISTRO USUARIO


def registro_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')  # Redirecionar para a página de login após o registro bem-sucedido
    else:
        form = UserCreationForm()
    return render(request, 'registro_user.html', {'form': form})

def login_view(request):
    error_message = None

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('perfil')  # Redireciona para a página de perfil após o login bem-sucedido
        else:
            error_message = 'Credenciais inválidas. Por favor, tente novamente.'

    return render(request, 'login.html', {'error_message': error_message})

@login_required
def perfil_view(request):
    # Lógica para exibir a página de perfil
    return render(request, 'perfil.html')

def logout_view(request):
    logout(request)
    return redirect('index') 