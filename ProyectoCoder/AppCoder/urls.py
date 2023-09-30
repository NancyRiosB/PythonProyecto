from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio),
    path('profesores', views.profesores, name='Profesores'),
    path('entregables', views.entregables, name='Entregables'),
    path('estudiantes', views.estudiantes, name='Estudiantes'),
    path('leerprofesores', views.leerProfesores, name='LeerProfesores'),
    path('cursos', views.cursos, name='Cursos'),
    path('busquedaCamada', views.busquedaCamada, name='BusquedaCamada'),
    path('buscar/', views.buscar),
    path('eliminarProfesor/<profesor_nombre>',
         views.borrarProfesores, name='EliminarProfesor'),
    path('editarProfesor/<profesor_nombre>',
         views.editarProfesores, name='EditarProfesor'),
    path('curso/list', views.CursoList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)/$', views.CursoDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.CursoCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)/$', views.CursoUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)/$', views.CursoDelete.as_view(), name='Delete'),

]
