from django.db import models
from django.utils.timezone import now
# Create your models here.
class Courses(models.Model):
    title=models.CharField(max_length=50, verbose_name="Título")
    image=models.ImageField(null=True,blank=True,upload_to='courses/', verbose_name='Imagen')
    link=models.URLField(null=True,blank=True,verbose_name="Dirección Web")


    created=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated=models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name='Curso'
        verbose_name_plural='Cursos'
        ordering=["-created"]
    def __str__(self):
        return self.title