from django.urls import path

from . import views


app_name = 'favoritos_app'

urlpatterns = [
    path('perfil-usuario/', views.UserPageListView.as_view(), name='perfil'),
    path('agregar-favoritos/<pk>/', views.AddFavoritosView.as_view(), name='add_favoritos'),
    path('eliminar-favoritos/<pk>/', views.FavoritosDeleteView.as_view(), name='eliminar_favorito'),

]
