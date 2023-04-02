from rest_framework import serializers
from app.models import Estado, Cidade, ClimaCidade

class EstadoSerializer (serializers.ModelSerializer):
    class Meta: 
        model = Estado
        fields = '__all__' # pegando todos os campos


class CidadeSerializer (serializers.ModelSerializer):
    class Meta: 
        model = Cidade
        fields = '__all__' # pegando todos os campos
        

class ClimaCidadeSerializer (serializers.ModelSerializer):
    class Meta: 
        model = ClimaCidade
        fields = '__all__' # pegando todos os campos
        read_only_fields = ['cidade', 'descricao']
    
        

      