from django.urls import path
from . import views


urlpatterns = [

    path('', views.lista_vagas, name='lista_vagas'),

    path('vaga/<int:vaga_id>/', views.detalhe_vaga, name='detalhe_vaga'),

    path('cadastrar/', views.cadastrar_vaga, name='cadastrar_vaga'),

    path('candidatar/<int:vaga_id>/', views.candidatar, name='candidatar'),

]