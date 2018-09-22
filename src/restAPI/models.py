from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
import uuid


def jwt_get_secret_key(user_model):
    return user_model.jwt_secret

class RestUserManager(BaseUserManager):
    def create_user(
        self, email, username, full_name, profile_picture=None, gender=None,
        password=None, is_admin=False, is_staff=False, is_active=True):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not full_name:
            raise ValueError("User must have a full name")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.username = username
        user.full_name = full_name
        user.set_password(password)  # change password to hash
        # user.profile_picture = profile_picture
        user.gender = gender
        user.admin = is_admin
        user.profile_picture = profile_picture
        user.staff = is_staff
        user.active = is_active
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, profile_picture, gender, full_name, password=None):
        user = self.create_user(
            email,
            full_name,
            profile_picture,
            gender,
            password=password,
            is_staff=True,
        )
        return user

    def create_superuser(self, email, full_name, profile_picture, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not full_name:
            raise ValueError("User must have a full name")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.full_name = full_name
        user.set_password(password)
        user.profile_picture = profile_picture
        user.admin = True
        user.staff = True
        user.active = True
        user.save(using=self._db)
        return user


class RestUser(AbstractBaseUser):
    username = models.CharField(max_length=30)
    full_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=255, unique=True,)
    gender = models.CharField(max_length=20, blank=True, default='rather_not_say')
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser
    jwt_secret = models.UUIDField(default=uuid.uuid4)
    # notice the absence of a "Password field", that's built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'username']  # Email & Password are required by default.

    objects = RestUserManager()

    def get_full_name(self):
        return self.full_name

    def __str__(self):
         return self.email

    @property
    def is_staff(self):
         return self.staff

    @property
    def is_admin(self):
         return self.admin

    @property
    def is_active(self):
         return self.active
