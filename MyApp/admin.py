from django.contrib import admin
from MyApp.models import *

# Register your models here.

admin.site.register(Producto)
admin.site.register(Desarrollador)
admin.site.register(Comprador)
admin.site.register(Vendedor)