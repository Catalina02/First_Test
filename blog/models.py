from django.db import models
from django.utils import timezone
'''
Modelar Clases que se pueden encontrar en la WebApp
ejemplo Post:
 _______________
|Post           |
|---------------|  
|Atributos  :   |
|title          |
|text           |
|author         |
|created_date   |
|published_date |
|---------------|
|Metodos:       |
|Publish        |
|_______________|
'''


class Post(models.Model): 
    '''
    models.Model=Post es un modelo de Django,así sabe que debe guardarlo en la base de datos.
    models.CharField=  texto con un número limitado de caracteres
    models.TextField= texto largo sin límite
    models.DateTimeField= formatos para fecha y hora.
    modelos.ForeignKey= relación (link) con otro modelo.
    '''
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title