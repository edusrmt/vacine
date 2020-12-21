from django.core.exceptions import ValidationError

def validade_only_digits(value):
  if value.isdigit() == False:
    raise ValidationError(
      f'Certifique-se de que este campo contenha apenas números',
      params={'value': value},
    )