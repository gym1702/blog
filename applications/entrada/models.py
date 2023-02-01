from django.db import models
from django.conf import settings

from .managers import EntryManager

from ckeditor_uploader.fields import RichTextUploadingField

#INSTALAR PRIMERO django-model-utils
from model_utils.models import TimeStampedModel


#MODELO DE CATEGORIA
class Category(TimeStampedModel):

    short_name = models.CharField('Nombre corto', max_length=50)
    name = models.CharField('Nombre', max_length=50)

    class Meta:
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name


#MODELO DE TAG
class Tag(TimeStampedModel):

    name = models.CharField('Nombre', max_length=50)

    class Meta:
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name


#MODELO DE ENTRADA
class Entry(TimeStampedModel):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Usuario')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoria')
    tag = models.ManyToManyField(Tag)
    title = models.CharField('Titulo de la entrada', max_length=200)
    resume = models.TextField('Resumen', blank=True, null=True)
    content = RichTextUploadingField('Contenido', blank=True, null=True)    
    image = models.ImageField('Imagen', upload_to='Entry', blank=True, null=True)
    public = models.BooleanField('Publico', default=False)
    area_trabajo = models.BooleanField('area de trabajo', default=False)
    marcas = models.BooleanField('En marca', default=False)
    in_home = models.BooleanField('En home', default=False)
    in_reciente = models.BooleanField('En recientes', default=False)
    ours = models.BooleanField('En nosotros', default=False)
    slug = models.SlugField(editable=False, max_length=300)
    
    class Meta:
        verbose_name_plural = 'Entradas'

    #Llamada a los managers
    objects = EntryManager()

    def __str__(self):
        return self.title
