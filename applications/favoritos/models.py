from django.db import models
from django.conf import settings

#INSTALAR PRIMERO django-model-utils
from model_utils.models import TimeStampedModel

from applications.entrada.models import Entry
from .managers import FavotitesManager



#MODELO DE FAVORITOS
class Favorites(TimeStampedModel):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    entry = models.ForeignKey(Entry, related_name='Entradas_favoritas', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Favoritos'
        unique_together = ['user', 'entry'] #solo permite un registro de usuario con una entrada especifica

    #PAra manejo de los managers
    objects = FavotitesManager()

    def __str__(self):
        return self.entry.title
