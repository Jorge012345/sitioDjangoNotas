from django.db import models

# Create your models here.

class News(models.Model):
    title=models.CharField(max_length=50, verbose_name="Título")
    image=models.ImageField(upload_to='activities/news/', verbose_name='Imagen')
    paragraph1=models.TextField(null=True,blank=True,max_length=700, verbose_name="Parrafo 1") 
    paragraph2=models.TextField(null=True,blank=True,max_length=700, verbose_name="Parrafo 2")       
    paragraph3=models.TextField(null=True,blank=True,max_length=700, verbose_name="Parrafo 3")       
    paragraph4=models.TextField(null=True,blank=True,max_length=700, verbose_name="Parrafo 4")       
    paragraph5=models.TextField(null=True,blank=True,max_length=700, verbose_name="Parrafo 5")             


    created=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated=models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name='Noticia'
        verbose_name_plural='Noticias'
        ordering=["-created"]
    def __str__(self):
        return self.title
        

class Videos(models.Model):
    title=models.CharField(max_length=50, verbose_name="Título")
    link=models.URLField(null=True,blank=True,max_length=300,verbose_name="Dirección Web")
    fichero=models.FileField(null=True,blank=True,upload_to='activities/videos/',verbose_name="Fichero")
    created=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated=models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')
    class Meta:
        verbose_name='Video'
        verbose_name_plural='Videos'
        ordering=["-created"]
    def __str__(self):
        return self.title

