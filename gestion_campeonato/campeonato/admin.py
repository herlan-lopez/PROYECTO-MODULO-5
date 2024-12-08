from django.contrib import admin
from .models import Equipo, Jugador, Campeonato, Inscripcion

# Registrar modelos en el administrador de Django

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre_eq', 'ciudad')

@admin.register(Jugador)
class JugadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'fecha_nac','posicion_juego','celular', 'equipo')
    search_fields = ('nombre','apellido','posicion_juego','equipo__nombre_eq')
    list_filter = ('nombre', 'apellido')

@admin.register(Campeonato)
class CampeonatoAdmin(admin.ModelAdmin):
    list_display = ('nombre_cam', 'fecha_inicio', 'fecha_fin', 'premio_economico')
    search_fields = ('nombre_cam',)
    list_filter = ('fecha_inicio', 'fecha_fin')

@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('jugador', 'campeonato', 'fecha_inscripcion')
    search_fields = ('jugador__nombre', 'jugador__apellido','campeonato__nombre_cam')
    list_filter = ('fecha_inscripcion',)