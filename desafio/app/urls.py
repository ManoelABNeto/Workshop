from rest_framework import routers
from app.views import EstadoViewSet, CidadeViewSet, ClimaViewSet

router = routers.DefaultRouter()
router.register(r'estado', EstadoViewSet)
router.register(r'cidade', CidadeViewSet)
router.register(r'clima', ClimaViewSet)

urlpatterns = router.urls
