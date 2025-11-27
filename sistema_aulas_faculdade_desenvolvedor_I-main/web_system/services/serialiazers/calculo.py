from rest_framework import serializers
from services.enumerations import Operations

class CalculoSerialiazer(serializers.Serializer):
    primeiro_termo = serializers.FloatField(required=True)
    segundo_termo = serializers.FloatField(required=True)
    operacao = serializers.ChoiceField(required=True, choices=Operations)

    resultado = serializers.CharField(required=False)

    class Meta:
        field = ['primeiro_termo','segundo_termo','operacao']

    def calculo(self):
        primeiro_termo = self.validated_data.get('primeiro_termo')
        segundo_termo = self.validated_data.get('segundo_termo')
        operacao = self.validated_data.get('operacao')

        match operacao:
            case Operations.ADDITION:
                self.validated_data.update({'resultado': primeiro_termo + segundo_termo})
                self.validated_data.update({'operacao': Operations.ADDITION.label})
            
            case Operations.SUBTRACTION:
                self.validated_data.update({'resultado': primeiro_termo - segundo_termo})
                self.validated_data.update({'operacao': Operations.SUBTRACTION.label})
            
            case Operations.MULTIPLICATION:
                self.validated_data.update({'resultado': primeiro_termo * segundo_termo})
                self.validated_data.update({'operacao': Operations.MULTIPLICATION.label})
            
            case Operations.DIVISION:
                self.validated_data.update({'resultado': primeiro_termo / segundo_termo})
                self.validated_data.update({'operacao': Operations.DIVISION.label})
            
            case _:
                raise NotImplementedError("Not Implemented")
