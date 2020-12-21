from rest_framework import viewsets
from rest_framework import permissions
from vacine.api.serializers import UserSerializer, PacienteSerializer
from vacine.api.models import User, Paciente
from django.db import transaction

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all().order_by('-date_joined')
  serializer_class = UserSerializer

class PacienteViewSet(viewsets.ModelViewSet):
  queryset = Paciente.objects.all().order_by('nome_completo')
  serializer_class = PacienteSerializer

  # def perform_create(self, serializer):
  #   validated_data = serializer.validated_data

  #   with transaction.atomic():
  #     email = validated_data.get('email', None)
  #     password = validated_data.get('password', None)

  #     user = User(email=email, password=password, user_type=1)
  #     user.clean()
  #     user.save()

  #     serializer.save(user=user)