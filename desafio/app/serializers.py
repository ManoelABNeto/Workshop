from rest_framework import serializers
from app.models import Estado, Cidade

class EstadoSerializer (serializers.ModelSerializer):
    class Meta: 
        model = Estado
        fields = '__all__' # pegando todos os campos


class CidadeSerializer (serializers.ModelSerializer):
    class Meta: 
        model = Cidade
        fields = '__all__' # pegando todos os campos
      