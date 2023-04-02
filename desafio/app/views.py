from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.pagination import PageNumberPagination
from app.serializers import EstadoSerializer, CidadeSerializer, ClimaCidadeSerializer
from app.models import Estado, Cidade, ClimaCidade
from app.service import WeatherApi
import os
import requests


API_WEATHER_KEY = os.getenv('API_WEATHER_KEY')


class CustomPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100


class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer
    pagination_class = CustomPagination
      
    
class CidadeViewSet(viewsets.ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer
    pagination_class = CustomPagination
    

class ClimaViewSet(viewsets.ModelViewSet):
    queryset = ClimaCidade.objects.all()
    serializer_class = ClimaCidadeSerializer
    pagination_class = CustomPagination
    

    def create(self, request):
        cidade_data = request.data.get('nome')
        cidade_query = CidadeViewSet.queryset.filter(nome=cidade_data).first()
        if not cidade_query:
            raise NotFound('Cidade não foi encontrada!')
        
        weather_model = WeatherApi.obtem_clima_por_cidade(cidade_data)
        clima_cidade = ClimaCidade(nome=weather_model.main, descricao=weather_model.description, cidade = cidade_query)
        clima_cidade.save()
        
        clima_cidade = self.get_serializer(clima_cidade)
        return Response(clima_cidade.data)
