from django.db import models

# Create your models here.
class Subjects(models.Model):
    header=models.CharField(max_length=100, verbose_name="Encabezamiento")
    title=models.CharField(max_length=100, verbose_name="Título")
    description=models.TextField(max_length=500, verbose_name="Descripción")
    fichero=models.FileField(null=True,blank=True,upload_to='subjects/',verbose_name="Fichero")
    created=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated=models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')



    class Meta:
        verbose_name='Asignatura'
        verbose_name_plural='Asignaturas'
        ordering=["-created"]
    def __str__(self):
        return self.title