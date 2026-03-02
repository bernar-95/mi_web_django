from django.urls import path
from .views import ListaPendientes, DetalleTareas, CrearTareas, EditarTareas, EliminarTareas, Logueo, PaginaRegistro
from django.contrib.auth.views import LogoutView

urlpatterns = [path('',ListaPendientes.as_view(),name='tareas'),
               path('login/', Logueo.as_view(), name='login'),
               path('logout/', LogoutView.as_view(next_page= 'login'), name='logout'),
               path('registro/', PaginaRegistro.as_view(), name='registro'),
               path('tarea/<int:pk>',DetalleTareas.as_view(),name='tarea'),
               path('crear-tarea/',CrearTareas.as_view(),name='crear-tarea'),
               path('editar-tarea/<int:pk>', EditarTareas.as_view(), name='editar-tarea'),
               path('eliminar-tarea/<int:pk>', EliminarTareas.as_view(), name='eliminar-tarea')]