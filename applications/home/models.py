from django.db import models

from .managers import HomeManager

#INSTALAR PRIMERO django-model-utils
from model_utils.models import TimeStampedModel


#MODELO DE PAGINA PRINCIPAL
class Home(TimeStampedModel):

    title_page = models.CharField('Titulo de la pagina', max_length=100)
    title = models.CharField('Encabezado', max_length=50, blank=True, null=True)
    subtitle = models.CharField('SubEncabezado', max_length=50, blank=True, null=True)
    description = models.TextField('Descripcion', blank=True, null=True)
    title_sec1 = models.CharField('Titulo secc 1', max_length=50, blank=True, null=True)
    title_sec2 = models.CharField('Titulo secc 2', max_length=50, blank=True, null=True)
    title_sec3 = models.CharField('Titulo secc 3', max_length=50, blank=True, null=True)
    title_sec4 = models.CharField('Titulo secc 4', max_length=50, blank=True, null=True)
    title_sec5 = models.CharField('Titulo secc 5', max_length=50, blank=True, null=True)
    about_text = models.TextField('Acerca de nosotros', blank=True, null=True)
    image_ours = models.ImageField('Imagen nosotros', upload_to='Portada', blank=True, null=True)
    email = models.EmailField('Email', blank=True, null=True)
    phone = models.CharField('Telefono', max_length=10)
    address = models.TextField('Direccion', blank=True, null=True)
    horario = models.CharField('Horario', max_length=100, blank=True, null=True)
    logo_principal = models.ImageField(upload_to='home', blank=True, null=True)
    logo_secundario = models.ImageField(upload_to='home', blank=True, null=True)
    image = models.ImageField('Imagen principal', upload_to='Portada', blank=True, null=True)
    red_social1 = models.CharField('Nombre Red Social 1', max_length=100, blank=True, null=True)
    link_red_social1 = models.CharField('Link Red Social 1', max_length=100, blank=True, null=True)
    logo_red_social1 = models.ImageField(upload_to='Logos', blank=True, null=True)
    red_social2 = models.CharField('Nombre Red Social 2', max_length=100, blank=True, null=True)
    link_red_social2 = models.CharField('Link Red Social 2', max_length=100, blank=True, null=True)
    logo_red_social2 = models.ImageField(upload_to='Logos', blank=True, null=True)
    red_social3 = models.CharField('Nombre Red Social 3', max_length=100, blank=True, null=True)
    link_red_social3 = models.CharField('Link Red Social 3', max_length=100, blank=True, null=True)
    logo_red_social3 = models.ImageField(upload_to='Logos', blank=True, null=True)
    red_social4 = models.CharField('Nombre Red Social 4', max_length=100, blank=True, null=True)
    link_red_social4 = models.CharField('Link Red Social 4', max_length=100, blank=True, null=True)
    logo_red_social4 = models.ImageField(upload_to='Logos', blank=True, null=True)
    public = models.BooleanField(default=False)
    

    class Meta:
        verbose_name_plural = 'Home'

    #Llamada a los managers
    objects = HomeManager()

    def __str__(self):
        return self.title_page


#MODELO DE SUSCRIPTORES
class Suscriber(TimeStampedModel):

    email = models.EmailField('Email de suscriptor')

    class Meta:
        verbose_name_plural = 'Suscriptores'

    def __str__(self):
        return self.email


#MODELO DE CONTACTO
class Contact(TimeStampedModel):

    full_name = models.CharField('Nombre', max_length=100)
    email = models.EmailField('Email de contacto')
    messagge = models.TextField('Mensaje')

    class Meta:
        verbose_name_plural = 'Contactos'

    def __str__(self):
        return self.full_name







