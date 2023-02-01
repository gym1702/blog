from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, View, DeleteView

from .models import Favorites
from applications.home.models import Home
from applications.entrada.models import Entry



class UserPageListView(LoginRequiredMixin, ListView):
    model = Favorites
    template_name = "perfil/perfil.html"
    context_object_name = 'entradas_user'
    login_url =  reverse_lazy('users_app:login')

    def get_queryset(self):
        return Favorites.objects.entradas_user(self.request.user)

    #contexto para cargar imagenes y logos de footer y navbar
    def get_context_data(self, **kwargs):
        context = super(UserPageListView, self).get_context_data(**kwargs)

        context["home"] = Home.objects.en_home()
        return context



class AddFavoritosView(LoginRequiredMixin, View):
    login_url =  reverse_lazy('users_app:login')

    def post(self, request, *args, **kwars):
            #recuperar usuario
        usuario = self.request.user
            #recuperar entrada de blog a agregar
        entrada = Entry.objects.get(id=self.kwargs['pk'])
            #crear registro
        Favorites.objects.create(
            user = usuario,
            entry = entrada,
        )

        return HttpResponseRedirect(reverse('favoritos_app:perfil'))



class FavoritosDeleteView(DeleteView):
    model = Favorites
    success_url = reverse_lazy('favoritos_app:perfil')



