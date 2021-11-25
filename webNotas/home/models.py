from django.db import models

# Create your models here.
class ImagesCover(models.Model):
    name=models.CharField(max_length=50, verbose_name="Nombre de portada")
    cover=models.ImageField(upload_to='home/covers/', verbose_name='Imagen')
    created=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated=models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')
    class Meta:
        verbose_name='Portada de imagen'
        verbose_name_plural='Portada de imagenes'
        ordering=["-created"]
    def __str__(self):
        return self.name
class Main(models.Model):
    title=models.CharField(max_length=100, verbose_name="Título")
    description=models.TextField(max_length=500, verbose_name="Descripción")  
    image=models.ImageField(upload_to='home/main/', verbose_name='Imagen')
    created=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated=models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')



    class Meta:
        verbose_name='Contenido principal'
        verbose_name_plural='Contenidos principales'
        ordering=["-created"]
    def __str__(self):
        return self.title