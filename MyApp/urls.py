from django.urls import path
from MyApp import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('buscar/', views.buscar),
    path('productos', views.productos, name='Productos'),
    path('desarrolladores', views.desarrolladores, name='Desarrolladores'),
    path('compradores', views.compradores, name='Compradores'),
    path('vendedores', views.vendedores, name='Vendedores'),
    path('login', views.login_request, name="Login"),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name='Logout')
]