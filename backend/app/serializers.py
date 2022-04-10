from rest_framework import serializers
from .models import Cidade, Estado


class CidadeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cidade
        fields = ['id', 'id_uf', 'nome','nome_uf',]


class EstadoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Estado
        fields = ['id', 'uf', 'nome',]
            
                
            
    

