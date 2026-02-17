from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario

# Creación de formularios de registro, este modelo es de mucha utilidad nos ahora mucho trabajo

class RegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2', ]

class LoginForm(AuthenticationForm):
    # No hace falta Meta
    pass