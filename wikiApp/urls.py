from django.urls import path
from . import views

app_name = 'wikiApp'

urlpatterns = [
    path('', views.vista_principal, name='vista_principal'),
    path('crear_tema/', views.crear_tema, name='crear_tema'),
    path('crear_articulo/', views.crear_articulo, name='crear_articulo'),
    path('temas/<int:tema_id>/', views.articulos_por_tema, name='articulos_por_tema'),
    path('articulo/<int:articulo_id>/', views.ver_articulo, name='ver_articulo'),
    path('buscar/', views.buscar_articulos, name='buscar_articulos'),
]