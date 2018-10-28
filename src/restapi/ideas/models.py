from django import forms
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.postgres.fields import ArrayField
from ..users.models import User as User
import uuid
import datetime

class Idea(models.Model):
	idea_name = models.CharField(max_length=35, unique=True)
	description = models.CharField(max_length=300)
	upvotes = models.IntegerField(default=0)
	require_assistance = models.BooleanField(default=False)
	owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='owner')
	created_on = models.DateTimeField(default=datetime.datetime.now())

	REQUIRED_FIELDS = ['idea_name', 'owner', 'description', 'require_assistance']

	def __str__(self):
		return self.idea_name

class Pinned_ideas(models.Model):
	user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='pinned_ideas')
	idea_list = ArrayField(models.CharField(max_length=20, blank=True), default=list)

class Upvoted_ideas(models.Model):
	user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='upvoted_ideas')
	idea_list = ArrayField(models.CharField(max_length=20, blank=True), default=list)
