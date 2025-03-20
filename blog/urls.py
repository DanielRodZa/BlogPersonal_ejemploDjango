from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_publicaciones, name='lista_publicaciones'),
    path('publicacion/<int:pk>/', views.detalle_publicacion, name='detalle_publicacion'),
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('categoria/<int:pk>/', views.detalle_categoria, name='detalle_categoria'),
]