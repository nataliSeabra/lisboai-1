from django.db import models

# Create your models here.

# retorno para status 
STATUS_CHOICES = (
    ('d', 'Rascunho'),
    ('p', 'Publicado'),    
)

ACTIVE_CHOICES = (
    ('a', 'Ativo'),
    ('d', 'Inativo'),    
)

class Categories(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100,blank=True)
    active = models.CharField(max_length=1, choices=ACTIVE_CHOICES)

    def __unicode__(self): 
        return (self.name)


class Article(models.Model):

    categories = models.ForeignKey('Categories',on_delete=False)
    short_description = models.CharField(max_length=100)
    description = models.TextField(max_length=100,blank=True)

    def __unicode__(self): 
        return (self.short_description)


class Social(models.Model):

    name = models.CharField(max_length=100)
    link = models.URLField(max_length=200,null=True, blank=True)

    def __unicode__(self): 
        return (self.name)
