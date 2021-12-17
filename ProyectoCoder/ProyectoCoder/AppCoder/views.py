from django.shortcuts import render

from django.http import HttpResponse

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from AppCoder.models import Estadio, Equipo, Empleado, Jugador, Curso

from AppCoder.forms import EstadioFormulario, EmpleadoFormulario, JugadorFormulario

# Create your views here.

#Primer vista
def inicio(request):

    #return HttpResponse('Esto es una prueba del inicio')
    return render(request, 'AppCoder/inicio.html')


def jugadores(request):

    return render(request, 'AppCoder/jugadores.html')


def equipos(request):

    return render(request, 'AppCoder/equipos.html')


def servicios(request):

    return render(request, 'AppCoder/servicios.html')


def estudiantes(request):

    return render(request, 'AppCoder/estudiantes.html')


def profesores(request):

    return render(request, 'AppCoder/profesores.html')


def entregables(request):

    return render(request, 'AppCoder/entregables.html')


def estadioFormulario(request):

    if request.method == 'POST':

        miFormulario = EstadioFormulario(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            estadioInsta = Estadio(direccion=informacion['direccion'], anioFund=informacion['anioFund'])

            estadioInsta.save()

            return render(request, 'AppCoder/inicio.html')


    else:

        miFormulario = EstadioFormulario()

    return render(request, 'AppCoder/estadioFormulario.html', {'miFormulario': miFormulario})

    #esta vista obtiene la informacion cuando se carga la direccion y el anioFund


def busquedaEquipo(request):

    return render(request, 'AppCoder/busquedaEquipo.html')



def buscar(request):

    if request.GET["nombre"]:

        nombre = request.GET["nombre"]

        equipo = Equipo.objects.filter(nombre__icontains=nombre)


        #respuesta = f"Estoy buscando a: {request.GET['nombre']}"


        return render(request, 'AppCoder/resultadoBusqueda.html')


    else:

        respuesta = "Che, mandame informacion"

    return HttpResponse(respuesta)








def empleadoFormulario(request):

    #Si desde el HTML me envían un método POST
    if request.method == 'POST':
        #ESTE FORMULARIO SE VA A GENERAR CON TODOS LOS DATOS QUE NOS ENVIARON CON EL METODO POST
        miFormulario = EmpleadoFormulario(request.POST)

        #SI SE PUDO ENTRAR AL  FORMULARIO - ENTRAMOS AL IF
        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            emple = Empleado(

                nombre = informacion['nombre'],
                apellido = informacion['apellido'],
                dni = informacion['dni'],
                profesional = informacion['profesional'],
                fechaDeNacimiento = informacion['fechaDeNacimiento']

            )

            emple.save() #ES EL COMANDO QUE PERMITE SALVAR EN LA BASE DE DATOS

            return render(request, 'AppCoder/inicio.html')


    else:

        miFormulario = EmpleadoFormulario()

    return render(request, 'AppCoder/empleadoFormulario.html', {'miFormulario': miFormulario})





def leerJugadores(request):

    jugadores = Jugador.objects.all()

    dir = {"jugadores": jugadores} #contexto

    return render(request, 'AppCoder/leerJugadores.html', dir)



def eliminarJugador(request, numero_para_borrar):

    jugadorQueQuieroBorrar = Jugador.objects.get(numero=numero_para_borrar)
    jugadorQueQuieroBorrar.delete()

    jugadores = Jugador.objects.all()

    return render(request, 'AppCoder/leerJugadores.html', {'jugadores':jugadores})




def editarJugador(request, numero_para_editar):

    jugador = Jugador.objects.get(numero=numero_para_editar) #ese numero par editar es el id de la base de datos

    if request.method == 'POST':

        miFormulario = JugadorFormulario(request.POST)


        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            jugador.apellido = informacion['apellido'],
            jugador.numero = informacion['numero'],
            jugador.esBueno = informacion['esBueno'],

            jugador.save()

            return render(request, 'AppCoder/inicio.html')

    else:

        miFormulario = JugadorFormulario(initial={"apellido":jugador.apellido, "numero":jugador.numero, "esBueno":jugador.esBueno})

    return render(request, 'AppCoder/editarJugador.html', {"miFormulario":miFormulario, "numero_para_editar":numero_para_editar})


def jugadorFormulario(request):


    if request.method == 'POST':

        miFormulario = JugadorFormulario(request.POST)


        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            juga = Jugador(

                apellido = informacion['apellido'],
                numero = informacion['numero'],
                esBueno = informacion['esBueno'],


            )

            juga.save()

            return render(request, 'AppCoder/inicio.html')


    else:

        miFormulario = JugadorFormulario(initial={"apellido":jugador.apellido, "numero":jugador.numero, "esBueno":jugador.esBueno})

    return render(request, 'AppCoder/jugadorFormulario.html', {'miFormulario': miFormulario})


#cbv clase basadas en vistas
# HACER CRUD CON "CURSO"

# ESTO ES EL EQUIVALENTE AL LEER ---> ESTA CLASE NOS DA TODOS LOS CURSOS Object Filter All
class CursoList(ListView):

    model = Curso
    template_name = 'AppCoder/cursos_list.html'

class CursoDetalle(DetailView):
    
    model = Curso
    template_name = 'AppCoder/curso_detalle.html'


class CursoCreacion(CreateView):
    
    model = Curso
    success_url = '../curso/list'
    fields = ["nombre", "camada", "esNoche"]
    

class CursoUpdate(UpdateView):
    
    model = Curso
    success_url = '../curso/list'
    fields = ["nombre", "camada","esNoche"]
    

class CursoDelete(DeleteView):
    model = Curso
    success_url = '../curso/list'
    