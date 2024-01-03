from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import EmailValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from .managers import UserManager

NULLABLE = {'null': True, 'blank': True}


class User(AbstractBaseUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Email', validators=[EmailValidator])

    first_name = models.CharField(max_length=35, verbose_name='First Name', **NULLABLE, )
    last_name = models.CharField(max_length=35, verbose_name='Last Name', **NULLABLE, )
    phone = PhoneNumberField(max_length=35, verbose_name='Phone', **NULLABLE, region='RU', )
    image = models.ImageField(upload_to='media/', verbose_name='Avatar', **NULLABLE, )

    is_active = models.BooleanField(default=True, verbose_name='Active Status', )
    is_admin = models.BooleanField(default=False, verbose_name='Staff Status', )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    class Meta:
        ordering = ()
        verbose_name = 'User'
        verbose_name_plural = 'Users'
