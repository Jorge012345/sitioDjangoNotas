from django.db import models

# Create your models here.
class Projects(models.Model):
    title=models.CharField(max_length=100, verbose_name="Título")
    description=models.TextField(max_length=500, verbose_name="Descripción")    
    link=models.URLField(null=True,blank=True,verbose_name="Dirección Web")
    fichero=models.FileField(null=True,blank=True,upload_to='projects/',verbose_name="Fichero")
    image=models.ImageField(upload_to='projects/', verbose_name='Imagen')
    created=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated=models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')



    class Meta:
        verbose_name='Proyecto'
        verbose_name_plural='Proyectos'
        ordering=["-created"]
    def __str__(self):
        return self.title