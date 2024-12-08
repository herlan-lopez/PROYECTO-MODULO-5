from django.db import models
from django.core.exceptions import ValidationError
from datetime import date
import re

def validar_celular(value):
    """Valida que el número de celular tenga 8 dígitos y comience con 6 o 7."""
    if not re.match(r'^[67]\d{7}$', value):
        raise ValidationError("El número de celular debe tener 8 dígitos y comenzar con 6 o 7.")


def validar_fechanaci(value):
    """Valida que la fecha de nacimiento asegure al menos 4 años de edad."""
    today = date.today()
    age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    if age < 4:
        raise ValidationError("El jugador debe tener al menos 4 años de edad.") 
    
def validar_texto(value):
    """Valida que el texto tenga una longitud mínima de 3 caracteres."""
    if len(value) < 3:
        raise ValidationError(("El texto debe tener al menos 3 caracteres."))
    
def validar_numero_positivo(valor):
    """Validar que el premio sea positivo."""
    if valor <= 0:
        raise ValidationError("El premio debe ser positivo.")
    

POSICIONES_JUEGO = [
    ('', 'Seleccione una posición'),
    ('ARQUERO', 'ARQUERO'),
    ('DEFENSOR', 'DEFENSOR'),
    ('MEDIOCAMPO', 'MEDIOCAMPO'),
    ('DELANTERO', 'DELANTERO'),
]
    
# Modelos o tablas
class Equipo(models.Model):
    nombre_eq = models.CharField(max_length=100, unique=True)
    ciudad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_eq

class Jugador(models.Model):
    nombre = models.CharField(max_length=100, validators=[validar_texto])
    apellido = models.CharField(max_length=100, validators=[validar_texto])
    fecha_nac = models.DateField(validators=[validar_fechanaci]) 
    posicion_juego = models.CharField(
        max_length=100,
        choices=POSICIONES_JUEGO,   
    )
    celular = models.CharField(max_length=8, validators=[validar_celular]) 
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='jugadores')

    def __str__(self):
        return f"{self.nombre} {self.apellido} "

class Campeonato(models.Model):
    nombre_cam = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    premio_economico = models.IntegerField(validators=[validar_numero_positivo])

    def __str__(self):
        return self.nombre_cam

class Inscripcion(models.Model):
 
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE, related_name='inscripciones')
    campeonato = models.ForeignKey(Campeonato, on_delete=models.CASCADE, related_name='inscripciones')
    fecha_inscripcion = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('jugador', 'campeonato')

    def __str__(self):
        return f"{self.jugador} inscrito en {self.campeonato}"
