from django import forms
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.postgres.forms import SimpleArrayField
from ..users.models import User as User
from ..ideas.models import Idea as Idea
import uuid
import datetime

class Comments(models.Model):
	text = models.CharField(max_length=500, default='NULL')
	user = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='user', null=True)
	idea = models.ForeignKey(Idea, on_delete=models.DO_NOTHING, db_column='idea', null=True)
	likes = models.IntegerField(default=0)
	dislikes = models.IntegerField(default=0)
	commented_at = models.DateTimeField(default=datetime.datetime.now())

	REQUIRED_FIELDS = ['text', 'user', 'idea']
	def __str__(self):
		return self.text

class Replies(models.Model):
	text = models.CharField(max_length=500)
	comment = models.ForeignKey('Comments', on_delete=models.DO_NOTHING, db_column='comment')
	user = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='user')
	likes = models.IntegerField(default=0)
	dislikes = models.IntegerField(default=0)
	replied_at = models.DateTimeField(default=datetime.datetime.now())

	REQUIRED_FIELDS = ['text', 'comment', 'user']
	def __str__(self):
		return self.text
