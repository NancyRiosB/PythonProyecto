from django.db import models


class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    camada = models.CharField(max_length=50)

    def __str__(self):
        return f'Curso: {self.nombre} - Camada: {self.camada}'


class Estudiante(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f'Estudiante: {self.nombre} {self.apellido} Email: {self.email}'


class Profesor(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField()
    profesion = models.CharField(max_length=40)

    def __str__(self):
        return f'Profesor: {self.nombre} {self.apellido} Email: {self.email} Area: {self.profesion}  '


class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()

    def __str__(self):
        estado_entrega = "Entregado" if self.entregado else "No Entregado"
        return f'Entregable: {self.nombre} - Fecha de Entrega: {self.fechaDeEntrega} - Estado: {estado_entrega}'
