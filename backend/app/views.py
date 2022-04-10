from pprint import pprint
from urllib import request
from django.http import JsonResponse, QueryDict
from .models import Estado, Cidade
from rest_framework.viewsets import ModelViewSet
from .serializers import CidadeSerializer, EstadoSerializer
from rest_framework.response import Response




#queryset =  Cidade.objects.all()
#for i in queryset:
#        print(i.id_uf.id)

class EstadoViewSet(ModelViewSet):
    queryset =  Estado.objects.all()
    serializer_class = EstadoSerializer


qs_Estado = EstadoViewSet.queryset


class CidadeViewSet(ModelViewSet):
    serializer_class = CidadeSerializer
    queryset = Cidade.objects.all()
    qs_estado = qs_Estado
    qs_cidade = queryset
    for itemEst in qs_estado:
        for itemCid in qs_cidade:
            if itemEst.id == itemCid.id_uf.id:
                qs_cidade.filter(id=itemCid.id).update(nome_uf=itemEst.nome)
    queryset = Cidade.objects.all()





