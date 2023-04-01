from rest_framework import routers
from app.views import EstadoViewSet, CidadeViewSet

router = routers.DefaultRouter()
router.register(r'estado', EstadoViewSet)
router.register(r'cidade', CidadeViewSet)

urlpatterns = router.urls