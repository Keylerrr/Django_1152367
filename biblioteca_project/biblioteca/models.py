from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator

def validar_autor(value):
    if not value or str(value).strip() == "":
        raise ValidationError('El nombre del autor no puede estar vacío.')
    
def validar_resumen(value):
    if value is None or len(value.strip()) < 15 :
        raise ValidationError('El resumen debe tener al menos 15 caracteres.')

def validar_calificacion(value):
    if value < 1 or value > 5:
        raise ValidationError(
            f'{value} no es una calificación válida. Debe estar entre 1 y 5.'
        )

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libros')
    fecha_publicacion = models.DateField()
    resumen = models.TextField()

    def __str__(self):
        return self.titulo
    
class Resena(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='resenas')
    texto = models.TextField()             
    calificacion = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)]
    )
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.libro.titulo} - {self.calificacion}/5"