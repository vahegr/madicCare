from django.db import models
from .managers import UserManager
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    username = models.CharField(
        max_length=50,
        unique=True,
    )
    full_name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    phone = models.CharField(
        max_length=12,
        unique=True,
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to='images/users',
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(
        default=True,
    )
    is_admin = models.BooleanField(
        default=False,
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        " Is the user a member of staff? "
        # Simplest possible answer: All admins are staff
        return self.is_admin