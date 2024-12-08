from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Equipo, Jugador, Campeonato, Inscripcion
from .serializers import EquipoSerializer, JugadorSerializer, CampeonatoSerializer, InscripcionSerializer


# ViewSet para gestionar los Equipos
class EquipoViewSet(viewsets.ModelViewSet):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer
    
# ViewSet para gestionar los Jugadores
class JugadorViewSet(viewsets.ModelViewSet):
    queryset = Jugador.objects.all()
    serializer_class = JugadorSerializer

# ViewSet para gestionar los Campeonatos
class CampeonatoViewSet(viewsets.ModelViewSet):
    queryset = Campeonato.objects.all()
    serializer_class = CampeonatoSerializer




# Custom API para listar las inscripciones de jugadores a campeonatos
class CustomInscripcionesAPIView(APIView):
    def get(self, request):
        inscripciones = Inscripcion.objects.select_related('jugador', 'campeonato')
        data = [
            {
                "jugador": f"{inscripcion.jugador.nombre} {inscripcion.jugador.apellido}",
                "campeonato": inscripcion.campeonato.nombre_cam,
                "fecha_inscripcion": inscripcion.fecha_inscripcion,
            }
            for inscripcion in inscripciones
        ]
        return Response(data)

