from vacine.api.models import User, Paciente
from rest_framework import serializers
from vacine.api.validators import validade_only_digits
from django.db import transaction
from django.db import IntegrityError

class UserSerializer(serializers.Serializer):
  email = serializers.EmailField(required=True)
  password = serializers.CharField(write_only=True)
  user_type = serializers.ChoiceField(User.USER_TYPE_CHOICES)

  def create(self, validated_data):
    return User.objects.create(**validated_data)

class PacienteSerializer(serializers.Serializer):
  id = serializers.IntegerField(read_only=True)
  nome_completo = serializers.CharField(required=True, allow_blank=False, max_length=255)
  cpf = serializers.CharField(required=True, allow_blank=False, max_length=11, validators=[validade_only_digits])
  data_nascimento = serializers.DateField()
  cns = serializers.CharField(required=True, allow_blank=False, max_length=15, validators=[validade_only_digits])
  user = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

  email = serializers.EmailField(write_only=True, required=True)
  password = serializers.CharField(write_only=True, required=True)

  def create(self, validated_data):
    with transaction.atomic():
      email = validated_data.pop('email')
      password = validated_data.pop('password')
      
      try:
        user = User(email=email, password=password, user_type=1)
        user.clean()
        user.save()
      except IntegrityError:
        raise serializers.ValidationError(detail='Não foi possível criar um usuário com essas credenciais')

      return Paciente.objects.create(user=user, **validated_data)