from django.shortcuts import render
from AppCoder.models import *
from django.http import HttpResponse
from django.views.generic import ListView
from AppCoder.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.


def inicio(request):
    return render(request, 'AppCoder/padre.html')


def leerProfesores(request):
    profesores = Profesor.objects.all()
    contexto = {'profesores': profesores}
    return render(request, 'AppCoder/leerProfesores.html', contexto)


def borrarProfesores(request, profesor_nombre):
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    profesor.delete()
    profesores = Profesor.objects.all()
    contexto = {'profesores': profesores}
    return render(request, 'AppCoder/leerProfesores.html', contexto)


def editarProfesores(request, profesor_nombre):
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            profesor.nombre = informacion['nombre']
            profesor.apellido = informacion['apellido']
            profesor.email = informacion['email']
            profesor.profesion = informacion['profesion']
            profesor.save()
            return render(request, 'AppCoder/padre.html')
    else:
        miFormulario = ProfesorFormulario(initial={
                                          'nombre': profesor.nombre, 'apellido': profesor.apellido, 'email': profesor.email, 'profesion': profesor.profesion})
    return render(request, 'AppCoder/profesores.html', {'miFormulario': miFormulario, 'profesor_nombre': profesor_nombre})


def profesores(request):
    # Inicializa el formulario antes del bloque if
    miFormulario = ProfesorFormulario()

    if request.method == 'POST':
        # Corrige 'request.Post' a 'request.POST'
        miFormulario = ProfesorFormulario(request.POST)
        if miFormulario.is_valid():  # Agrega paréntesis a 'is_valid'
            informacion = miFormulario.cleaned_data
            profesor = Profesor(nombre=informacion['nombre'], apellido=informacion['apellido'],
                                email=informacion['email'], profesion=informacion['profesion'])  # Corrige la asignación de campos
            profesor.save()
            return render(request, 'AppCoder/padre.html')

    return render(request, 'AppCoder/profesores.html', {'miFormulario': miFormulario})


def cursos(request):
    miFormulario = CursoFormulario()

    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso = Curso(
                nombre=informacion['nombre'], camada=informacion['camada'])
            curso.save()
            return render(request, 'AppCoder/padre.html')

    return render(request, 'AppCoder/cursos.html', {'miFormulario': miFormulario})


def estudiantes(request):
    miFormulario = EstudianteFormulario()

    if request.method == 'POST':
        miFormulario = EstudianteFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            estudiante = Estudiante(
                nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'])
            estudiante.save()
            return render(request, 'AppCoder/padre.html')

    return render(request, 'AppCoder/estudiantes.html', {'miFormulario': miFormulario})


def entregables(request):
    miFormulario = EntregableFormulario()

    if request.method == 'POST':
        miFormulario = EntregableFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            entregable = Entregable(
                nombre=informacion['nombre'], fechaDeEntrega=informacion['fechaDeEntrega'], entregado=informacion['entregado'])
            entregable.save()
            return render(request, 'AppCoder/padre.html')

    return render(request, 'AppCoder/entregables.html', {'miFormulario': miFormulario})


def busquedaCamada(request):
    return render(request, 'AppCoder/busquedaCamada.html')


def buscar(request):
    if request.GET['camada']:
        camada = request.GET['camada']
        cursos = Curso.objects.filter(camada__icontains=camada)
        return render(request, 'AppCoder/resultadoBusqueda.html', {'cursos': cursos, 'camada': camada})
    else:
        return HttpResponse('Te equivocaste cabezon')


class CursoList(ListView):
    model = Curso
    template_name = 'AppCoder/cursoList.html'


class CursoDetalle(DetailView):
    model = Curso
    template_name = 'AppCoder/cursoDetalle.html'


class CursoCreacion(CreateView):
    model = Curso
    success_url = 'AppCoder/curso/list'
    fields = ['nombre', 'camada']


class CursoUpdate(UpdateView):
    model = Curso
    fields = ['nombre', 'camada']
    success_url = reverse_lazy('List')


class CursoDelete(DeleteView):
    model = Curso

    def get_success_url(self):
        return reverse_lazy('List')


class ProfesorList(ListView):
    model = Profesor
    template_name = 'AppCoder/profesor/list.html'


class ProfesorDetalle(DetailView):
    model = Profesor
    template_name = 'AppCoder/cursoDetalle.html'
