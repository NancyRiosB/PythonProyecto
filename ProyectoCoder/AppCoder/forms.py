from django import forms


class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=40)


class EntregableFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    fechaDeEntrega = forms.DateField()
    entregado = forms.BooleanField()


class EstudianteFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    email = forms.EmailField()


class CursoFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    camada = forms.CharField(max_length=50)
