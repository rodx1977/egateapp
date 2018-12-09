from django.contrib import admin

# Register your models here.

from .models import CategoriaProveedores, Proveedores, AutorizarProveedor

admin.site.register(CategoriaProveedores)
admin.site.register(Proveedores)
#admin.site.register(AutorizarProveedor)
