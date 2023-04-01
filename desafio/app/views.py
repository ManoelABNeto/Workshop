from rest_framework import viewsets
from app.serializers import ToDoSerializer
from app.models import Estado

class EstadoViewSet(viewsets.ModelViewSet):
    
    queryset = Estado.objects.all()
    serializer_class = ToDoSerializer
