from django.shortcuts import render, redirect
from .forms import RegistroUsuarioForm
from django.contrib.auth import login

def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Inicia sesión al registrarse
            return redirect('inicio')  # O redirige a donde quieras
    else:
        form = RegistroUsuarioForm()
    
    return render(request, 'registro.html', {'form': form})
