from django.urls import path
from .views import UsuarioList, UsuarioDetail, UsuarioCreate,UsuarioUpdate,UsuarioDelete

urlpatterns = [
    path('listar_user/', UsuarioList.as_view(), name='listar_usuario'),
    path('detalhar_user/<int:pk>/',
         UsuarioDetail.as_view(), name='detalhar_usuario'),
    path('criar_user/', UsuarioCreate.as_view(), name='criar_usuario'),
    path('atualizar_user/<int:pk>/',
         UsuarioUpdate.as_view(), name='atualizar_usuario'),
path('deletar_user/<int:pk>/',
         UsuarioDelete.as_view(), name='deletar_usuario'),

]
