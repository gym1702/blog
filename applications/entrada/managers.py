from django.db import models


class EntryManager(models.Manager):

    def areas_trabajo(self):
        return self.filter(public=True, area_trabajo =True).order_by('created')[:10]

    def trabajos_recientes(self):
        return self.filter(public=True, in_reciente=True).order_by('-created')[:4]
    
    def nosotros(self):
        return self.filter(public=True, ours=True).first()

    def buscar_entrada(self, kword, categoria):
        if len(categoria) > 0:
            return self.filter(category__short_name=categoria, title__icontains=kword, public=True).order_by('created')
        else:
            return self.filter(title__icontains=kword, public=True).order_by('created')
