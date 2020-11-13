from random import choice

from core.managers import CustomUserManager
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from djongo import models


class CustomUser(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    password = models.CharField(verbose_name=_('password'),
                                max_length=128
                                )
    last_login = models.DateTimeField(verbose_name=_('last login'),
                                      blank=True,
                                      null=True
                                      )
    username = models.CharField(verbose_name=_('username'),
                                max_length=150,
                                unique=True,
                                help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
                                validators=[username_validator],
                                error_messages={
                                    'unique': _("A user with that username already exists."),
                                },
                                null=True
                                )
    first_name = models.CharField(verbose_name=_('first name'),
                                  max_length=30,
                                  blank=True
                                  )
    last_name = models.CharField(verbose_name=_('last name'),
                                 max_length=150,
                                 blank=True
                                 )
    is_staff = models.BooleanField(verbose_name=_('staff status'),
                                   default=False,
                                   help_text=_('Designates whether the user can log into this admin site.'),
                                   )
    is_active = models.BooleanField(verbose_name=_('active'),
                                    default=True,
                                    help_text=_(
                                        'Designates whether this user should be treated as active. '
                                        'Unselect this instead of deleting accounts.'
                                    ),
                                    )
    date_joined = models.DateTimeField(verbose_name=_('date joined'),
                                       default=timezone.now
                                       )

    email = models.EmailField(verbose_name=_('Email адрес'),
                              unique=True,
                              error_messages={
                                  'unique': _("A user with that email already exists."),
                              },
                              )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    class Meta:
        verbose_name = 'Пользоатель'
        verbose_name_plural = 'Пользователи'
        ordering = ['-date_joined']

    def name(self):
        if self.first_name:
            if self.last_name:
                return self.get_full_name()
            else:
                return self.first_name
        else:
            first_name = ['Неопознаный', 'Загадочный', 'Новый', 'Странный']
            last_name = ['Лемур', 'Слон', 'Тигр', 'Кот', 'Якуар', 'Медведь', 'Динозавр']
            return '{first_name} {last_name}'.format(first_name=choice(first_name), last_name=choice(last_name))

    def __str__(self):
        return '{name} ({email})'.format(name=self.name(), email=self.email)
