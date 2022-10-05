from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator
from django.db import models

from .validators import username_validator

USER = 'user'
MODERATOR = 'moderator'
ADMIN = 'admin'

ROLES = [
    (USER, USER),
    (MODERATOR, MODERATOR),
    (ADMIN, ADMIN),
]


class User(AbstractUser):
    username = models.CharField(
        'Никнейм',
        validators=(username_validator,),
        max_length=150,
        unique=True,
        blank=False,
        null=False,
    )
    first_name = models.CharField(
        'Имя',
        max_length=150,
        blank=True
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=150,
        blank=True
    )
    email = models.EmailField(
        'Email',
        validators=(EmailValidator,),
        max_length=254,
        unique=True,
        blank=False,
        null=False,
    )
    role = models.CharField(
        'Роль пользователя',
        choices=ROLES,
        max_length=50,
        default=USER,
        blank=True
    )
    bio = models.TextField(
        'Биография',
        blank=True
    )
    confirmation_code = models.CharField(
        'Код подтверждения',
        max_length=254,
        null=True,
        blank=False,
        default='****'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('username', 'email'), name='unique_user'
            )
        ]
        ordering = ('username',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    REQUIRED_FIELDS = ['email']
    USERNAME_FIELDS = 'email'

    def __str__(self):
        return str(self.username)

    @property
    def is_admin(self):
        return self.role == ADMIN or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == MODERATOR

    @property
    def is_user(self):
        return self.role == USER
