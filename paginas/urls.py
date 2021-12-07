from django.views.generic import TemplateView
from django.urls import path
from django.contrib.auth import views as auth_views 
from . import views

urlpatterns = [
    path('', views.paginainicial),
    path('logar/', views.logar, name='logar'),
    path('logout/', views.logout_view, name='logout'),
    path('form-cadastro/', views.form_cadastro),
    path('principal/', views.paginaprincipal),
    path('cadastrar-usuario/', views.cadastrar_usuario, name="cadastro"),
    path('produto/', views.produto),
    path('login/', views.login),
    path('cadastrar-produto/', views.cadastrar_produto),
]
  