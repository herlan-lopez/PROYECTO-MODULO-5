from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from campeonato.views import EquipoViewSet, JugadorViewSet, CampeonatoViewSet, CustomInscripcionesAPIView

router = DefaultRouter()
router.register('equipos', EquipoViewSet)
router.register('jugadores', JugadorViewSet)
router.register('campeonatos', CampeonatoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/custom-inscripciones/', CustomInscripcionesAPIView.as_view()),
]
