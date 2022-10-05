from django.core.exceptions import ValidationError


def username_validator(value):
    if value == 'me':
        raise ValidationError(
            'Запрещено использование имени пользователя "me".',
            params={'value': value},
        )
