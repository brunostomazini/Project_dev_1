from rest_framework import serializers
from aula.models import Perfil



class PerfilMinimalSerializer(serializers.ModelSerializer):
    '''url = serializers.HyperlinkedIdentityField(
        view_name=,
        lookup_fields ='pk',
        read_only=true,
    )'''

    class Meta:
        model = Perfil
        fields = ['cidade', 'pais']

    def create(self, validated_data):
        return Perfil.objects.create(**validated_data)