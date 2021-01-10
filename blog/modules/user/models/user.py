from django.db.models import CharField, BigAutoField, EmailField, BooleanField
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser

from ..manager import BlogUserManager
from ...common.models.timestamp import TimeStampModel


class User(AbstractBaseUser, TimeStampModel, PermissionsMixin):
    class Meta:
        db_table = 'users'
        verbose_name = 'user'

    id = BigAutoField(primary_key=True)
    email = EmailField('email', max_length=255, unique=True)
    name = CharField('name', max_length=255)
    is_admin = BooleanField(default=False)
    is_staff = BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    objects = BlogUserManager()
