from django import forms
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.postgres.fields import ArrayField
from ..users.models import User as User

import uuid
import datetime


class Project(models.Model):
    project_name = models.CharField(max_length=35)
    project_id = models.CharField(max_length=35, unique=True)
    collaborators = ArrayField(models.CharField(max_length=20), default=list)
    description = models.CharField(max_length=300)
    owner = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, db_column='owner')
    created_on = models.DateTimeField(default=datetime.datetime.now())
    current_stage = models.CharField(max_length=20)
    area_of_issues_open = ArrayField(
        models.CharField(max_length=20), default=list)

    REQUIRED_FIELDS = ['project_name', 'owner',
                       'description', 'current_stage']

    def __str__(self):
        return self.project_name
