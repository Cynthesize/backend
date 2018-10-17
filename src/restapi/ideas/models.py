from django import forms
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.postgres.forms import SimpleArrayField
from ..users.models import User as User
import uuid
import datetime

class Pinned_ideas(models.Model):
	user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='pinned_ideas')
	idea = models.ForeignKey('Idea', on_delete=models.DO_NOTHING)

class Upvoted_ideas(models.Model):
	user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='upvoted_ideas')
	idea = models.ForeignKey('Idea', on_delete=models.DO_NOTHING)

class Idea(models.Model):
	idea_name = models.CharField(max_length=35, unique=True)
	description = models.CharField(max_length=300)
	upvotes = models.IntegerField(default=0)
	require_assistance = models.BooleanField(default=False)
	owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='owner')
	created_on = models.DateTimeField(default=datetime.datetime.now())

	REQUIRED_FIELDS = ['idea_name', 'owner', 'description', 'require_assistant']

	def __str__(self):
		return self.idea_name


class Comments(models.Model):
	comment_text = models.CharField(max_length=500, unique=True)
	commentator = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='commentator')
	likes = models.IntegerField(default=0)
	dislikes = models.IntegerField(default=0)
	is_parent = models.BooleanField(default=True)
	parent_comment = models.IntegerField(default=None)
	beneficial_comment = models.BooleanField(default=False)
	commented_on = models.DateTimeField(default=datetime.datetime.now())

	REQUIRED_FIELDS = ['comment_text', 'commentator']

	def __str__(self):
		return self.comment_text
