from django.contrib import admin
from .models import Categoria, Publicacion, Comentario

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Publicacion)
admin.site.register(Comentario)