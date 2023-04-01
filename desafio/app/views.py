from rest_framework import viewsets, status
from rest_framework.response import Response
from app.serializers import EstadoSerializer, CidadeSerializer
from app.models import Estado, Cidade


class EstadoViewSet(viewsets.ModelViewSet):
    
    # allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer
  
    def create(self, request):
        estado = self.get_serializer(data=request.data)
        estado.is_valid(raise_exception=True)
        estado.save()
        return Response(estado.data, status=status.HTTP_201_CREATED)
    
    
    
class CidadeViewSet(viewsets.ModelViewSet):
    
    # allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer
    
    # def create(self, request):
    #     cidade = self.get_serializer(data=request.data)
    #     cidade.is_valid(raise_exception=True)
    #     cidade.save()
    #     return Response(cidade.data, status=status.HTTP_201_CREATED)
