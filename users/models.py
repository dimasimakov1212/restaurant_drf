from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    VERSION_CHOICES = ((True, 'Действующий'), (False, 'Заблокирован'))

    user_email = models.EmailField(unique=True, verbose_name='почта')
    user_phone = models.CharField(max_length=35, verbose_name='телефон', blank=True, null=True)
    is_active = models.BooleanField(choices=VERSION_CHOICES, default=False, verbose_name='Статус пользователя')

    USERNAME_FIELD = "user_email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
