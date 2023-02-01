from django.shortcuts import render

from django.views.generic import ListView, TemplateView, DetailView

from .models import Entry, Category
from .managers import EntryManager

from applications.home.models import Home


#CLASS PARA BLOG
class EntryListView(ListView):
    template_name = "entrada/lista.html"
    context_object_name = 'entradas'
    paginate_by = 6

    #CONTEXTO NECESARIO PARA CARGAR IMAGENES Y DATOS EN FOOTER Y NAVBAR
    def get_context_data(self, **kwargs):
        context = super(EntryListView, self).get_context_data(**kwargs)

        #contexto para cargar variables en footer y navbar
        context["home"] = Home.objects.en_home()

        #contexto para categorias
        context["categorias"] = Category.objects.all()

        return context


    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        categoria = self.request.GET.get('categoria', '')
        #Consulta de busqueda
        resultado = Entry.objects.buscar_entrada(palabra_clave, categoria)
        return resultado



class EntryDetailView(DetailView):
    model = Entry
    template_name = "entrada/detalle.html"
    context_object_name = 'detalles'

    def get_context_data(self, **kwargs):
        context = super(EntryDetailView, self).get_context_data(**kwargs)

        #contexto para cargar variables en footer y navbar
        context["home"] = Home.objects.en_home()

        return context
