from django.contrib import admin
from .models import Simplex, Oferta, Demanda, Peso

# Register your models here.
admin.site.register(Simplex)
admin.site.register(Oferta)
admin.site.register(Demanda)
admin.site.register(Peso)