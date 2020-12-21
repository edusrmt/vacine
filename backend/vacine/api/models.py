from django.contrib.auth.models import AbstractUser
from django.db import models
from vacine.api.managers import UserManager
from vacine.api.validators import validade_only_digits

class User(AbstractUser):
  USER_TYPE_CHOICES = (
    (1, 'paciente'),
    (2, 'profissional'),
    (3, 'coordenador'),
  )

  username = None
  email = models.EmailField(unique=True)
  user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['user_type']

  objects = UserManager()

class Paciente(models.Model):
  nome_completo = models.CharField(max_length=255)
  cpf = models.CharField(max_length=11, validators=[validade_only_digits])
  data_nascimento = models.DateField()
  cns = models.CharField(max_length=15, validators=[validade_only_digits])
  user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

  class Meta:
    verbose_name = 'paciente'
    verbose_name_plural = 'pacientes'

  def __str__(self):
    cpf = '{}{}{}.{}{}{}.{}{}{}-{}{}'.format(*self.cpf)
    return f'{self.nome_completo} ({cpf})'