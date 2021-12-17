
from django.urls import path
from AppCoder import views


urlpatterns = [


    path('inicio', views.inicio, name='Inicio'),
    path('jugadores', views.jugadores, name='Jugadores'),
    path('equipos', views.equipos, name='Equipos'),
    path('servicios', views.servicios, name='Servicios'),
    path('estudiantes', views.estudiantes, name='Estudiantes'),
    path('profesores', views.profesores, name='Profesores'),
    path('entregables', views.entregables, name='Entregables'),
    path('estadioFormulario', views.estadioFormulario, name='EstadioFormulario'),
    path('busquedaEquipo', views.busquedaEquipo, name='BusquedaEquipo'),
    path('buscar/', views.buscar),
    path('empleadoFormulario', views.empleadoFormulario, name='EmpleadoFormulario'),
    path('leerJugadores', views.leerJugadores),
    path('eliminarJugador/<numero_para_borrar>', views.eliminarJugador, name='EliminarJugador'),
    path('editarJugador/<numero_para_editar>', views.editarJugador, name='EditarJugador'),
    path('jugadorFormulario', views.jugadorFormulario, name='jugadorFormulario'),
    path('curso/list', views.CursoList.as_view(), name='List'),
    #FALTA EL PATH DE CREATE, UPDATE Y DELETE


]