# app_cliente/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'), # <-- Aquí usas views.index y name='inicio'
    path('cliente/<int:cliente_id>/', views.ver_cliente, name='ver_cliente'),
    path('cliente/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('cliente/editar/<int:id>/', views.editar_cliente, name='editar_cliente'),
    path('cliente/borrar/<int:id>/', views.borrar_cliente, name='borrar_cliente'),
]