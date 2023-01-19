from django.shortcuts import render, HttpResponse
from MyApp.models import Producto, Desarrollador, Comprador, Vendedor
from MyApp.forms import *


# Create your views here.

def inicio(request):
    return render(request, 'MyApp/inicio.html')

def productos(request):
    if request.method == 'POST':
        miFormulario = ProductoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            producto = Producto(nombre=informacion['nombre'], genero=informacion['genero'], creador=informacion['creador'])
            producto.save()
            return render(request, "MyApp/inicio.html")
    else: 
        miFormulario= ProductoFormulario()
    return render(request, "MyApp/productos.html", {"miFormulario":miFormulario})

def desarrolladores(request):
    if request.method == 'POST':
        miFormulario = DesarrolladorFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            desarrollador = Desarrollador(nombre=informacion['nombre'])
            desarrollador.save()
            return render(request, "MyApp/inicio.html")
    else: 
        miFormulario= DesarrolladorFormulario()
    return render(request, "MyApp/desarrolladores.html", {"miFormulario":miFormulario})

def compradores(request):
    if request.method == 'POST':
        miFormulario = CompradorFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            comprador = Comprador(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'])
            comprador.save()
            return render(request, "MyApp/inicio.html")
    else: 
        miFormulario= CompradorFormulario()
    return render(request, "MyApp/compradores.html", {"miFormulario":miFormulario})

def vendedores(request):
    if request.method == 'POST':
        miFormulario = VendedorFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            vendedor = Vendedor(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'])
            vendedor.save()
            return render(request, "MyApp/inicio.html")
    else: 
        miFormulario= VendedorFormulario()
    return render(request, "MyApp/vendedores.html", {"miFormulario":miFormulario})

def buscar(request):
    if request.GET["nombre"]:
        nombre = request.GET['nombre'] 
        productos = Producto.objects.filter(nombre__icontains=nombre)
        return render(request, "MyApp/inicio.html", {"productos":productos, "nombre":nombre})
    else: 
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)

#Para el login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

#Para el login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():  # Si pasó la validación de Django
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username= usuario, password=contrasenia)
            if user is not None:
                login(request, user)
                return render(request, "MyApp/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "MyApp/inicio.html", {"mensaje":"Datos incorrectos"})      
        else:
            return render(request, "MyApp/inicio.html", {"mensaje":"Formulario erroneo"})
    form = AuthenticationForm()
    return render(request, "MyApp/login.html", {"form": form})

from MyApp.forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request,"MyApp/inicio.html" ,  {"mensaje":"Usuario Creado :)"})
    else:
        #form = UserCreationForm()       
        form = UserRegisterForm()     
    return render(request,"MyApp/registro.html" ,  {"form":form})

from django.contrib.auth.decorators import login_required

@login_required
def inicio(request):
    return render(request, "MyApp/inicio.html")