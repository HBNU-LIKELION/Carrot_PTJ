from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


class UserManager(BaseUserManager):
    def create_user(self, email, user_name, user_id, phone, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            user_name = user_name,
            user_id = user_id,
            phone = phone,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, user_name, user_id, phone, password):
        user = self.create_user(
            email,
            user_name=user_name,
            password=password,
            user_id = user_id,
            phone = phone,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='이메일',
        max_length=255,
        unique=True,
    )
    user_id = models.CharField(
        max_length=32, 
        unique=True, 
        verbose_name='유저 아이디'
    )
    user_name = models.CharField(
        max_length=10, 
        unique=False, 
        verbose_name='유저 이름'
    )
    phone = models.CharField(
        max_length=20, 
        unique=True, 
        verbose_name='전화번호'
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['user_name', 'phone', 'email']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin