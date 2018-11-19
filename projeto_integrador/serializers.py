from rest_framework import serializers
from projeto_integrador.models import *

class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = ('id', 'nome', 'intervalo', 'horario_Ini', 'qtd', 'limite', 'status')