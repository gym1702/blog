from django.urls import path

from . import views


app_name = 'entrada_app'

urlpatterns = [
    path('blogs/', views.EntryListView.as_view(), name='entradas'),
    path('detalle_blog/<pk>/', views.EntryDetailView.as_view(), name='detalle_entrada'),
]
