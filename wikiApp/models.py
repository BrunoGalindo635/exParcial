from django.db import models
from django import forms

# Create your models here.

class TemaWiki(models.Model):
    nombre = models.CharField(max_length=128)
    descripcion = models.TextField(max_length=512)

    def __str__(self):
        return self.nombre

class ArticuloWiki(models.Model):
    titulo = models.CharField(max_length=128)
    contenido = models.TextField(max_length=1024)
    temaRelacionado = models.ForeignKey(TemaWiki, on_delete=models.CASCADE, related_name='articulos')

    def __str__(self):
        return self.titulo
    
class TemaForm(forms.ModelForm):
    class Meta:
        model = TemaWiki
        fields = ['nombre', 'descripcion']

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = ArticuloWiki
        fields = ['titulo', 'contenido', 'temaRelacionado']