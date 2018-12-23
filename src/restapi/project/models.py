from django import forms
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.postgres.fields import ArrayField
from ..users.models import User as User

import uuid
import datetime


class Project(models.Model):
    """ Model for Project.

    Column Values:
        project_name: str. Name of the project.
        project_id: integer. ID of the project.
        collaborators: list(User). List of IDs of collaborators of the project
        description: str. Description of the project
        owner: User. ID of the owner of the project.
        created_on: timestamp. Timestamp of creation of project.
        current_stage: str. The current stage that the user can define for the project.
        area_of_issues_open: list(). 
        watching: list(User). List of users that are currently watching the project.
        endorsements: list(User). List of users that are in favor of the project.
    """
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
    watching = ArrayField(models.CharField(
        max_length=20, blank=True), default=list)
    endorsements = ArrayField(models.CharField(
        max_length=20, blank=True), default=list)
    timestamp = models.DateTimeField(default=datetime.datetime.now())

    REQUIRED_FIELDS = ['project_name', 'owner',
                       'description', 'current_stage']

    def __str__(self):
        return self.project_name


class Issue(models.Model):
    """ Model for Issue of each checkpoint.

    Column Values:
        checkpoint_name: str. Name of the checkpoint that the issue belongs to.
        comments: list(Comments). List of comments that belong to the issue.
        created_by: User. ID of the creator of the issue.
        created_on: timestamp. Timestamp of creation of project.
        description: str. Description of the idea.
        is_resolved: boolean. Whether the issue is resolved or active.
        project_id: Project. The ID of the project to which the issue belongs.
    """
    checkpoint_name = models.CharField(max_length=35)
    comments = ArrayField(models.CharField(
        max_length=20, blank=True), default=list)
    created_by = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, db_column='created_by')
    created_on = models.DateTimeField(default=datetime.datetime.now())
    description = models.CharField(max_length=200)
    is_resolved = models.BooleanField(default=False)
    project_id = models.ForeignKey(
        Project, on_delete=models.DO_NOTHING, db_column='project_id')


class IssueComment(models.Model):
    """ Model for comments on an issue.

    Column Values:
        comment_replies: list(Reply). List of replies for a comment.
        comment_text: str. The content of a text.
        commenter: User. The user who makes the comment.
        issue_id: Issue. ID of the issue.
        likes: int. Likes on the comment.
        previous_edits: list(str). Any previous edits on the comment.
        project_id: Project. ID of the project.
        timestamp: timestamp. Timestamp of creation of the issue .
    """
    comment_replies = ArrayField(models.CharField(
        max_length=25, blank=True), default=list)
    comment_text = models.TextField()
    commenter = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, db_column='commenter')
    issue_id = models.ForeignKey(
        Issue, on_delete=models.DO_NOTHING, db_column='issue_id')
    likes = models.IntegerField(default=0)
    previous_edits = ArrayField(models.TextField(), default=list)
    project_id = models.ForeignKey(
        Project, on_delete=models.DO_NOTHING, db_column='project_id')
    timestamp = models.DateTimeField(default=datetime.datetime.now())


class IssueReply(models.Model):
    """ Model for reply of a comment on an issue.

    Column Values:
        comment_id: IssueComment. ID of the comment.
        comment_text: str. The content of a text.
        respondent: User. The user who makes the respondent.
        likes: int. Likes on the comment.
        previous_edits: list(str). Any previous edits on the comment.
        timestamp: timestamp. Timestamp of creation of the issue .
    """
    comment_id = models.ForeignKey(
        IssueComment, on_delete=models.CASCADE, db_column='comment_id')
    reply_text = models.TextField()
    respondent = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, db_column='respondent')
    likes = models.IntegerField(default=0)
    previous_edits = ArrayField(models.TextField(), default=list)
    timestamp = models.DateTimeField(default=datetime.datetime.now())
