from django import forms
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.postgres.forms import SimpleArrayField
import uuid
import datetime


def jwt_get_secret_key(user_model):
	return user_model.jwt_secret


class UserManager(BaseUserManager):
	def create_user(self, username, full_name, email, password=None):
		"""
		Creates and saves a User with the given email and password.
		"""
		if not username:
			raise ValueError('Username must be present.')

		user = self.model(
			username=username,
			full_name=full_name,
			email=email
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, username, full_name, email, password):
		"""
		Creates and saves a superuser with the given email and
		password.
		"""
		user = self.create_user(
			username,
			password=password,
			full_name=full_name,
			email=email
		)
		user.is_admin = True
		user.is_staff = True
		user.save(using=self._db)
		return user


class User(AbstractBaseUser, PermissionsMixin):
	username = models.CharField(
		verbose_name='Username', max_length=35, unique=True)
	full_name = models.CharField(max_length=30, blank=True, null=True)
	email = models.EmailField(
			max_length=255, unique=True, blank=True, null=True)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)
	jwt_secret = models.UUIDField(default=uuid.uuid4)
	objects = UserManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['full_name', 'email']

	def __str__(self):
		return self.username
