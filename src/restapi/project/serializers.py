from rest_framework import serializers as serializer
from djoser import serializers
from . import models


class ProjectSerializer(serializer.ModelSerializer):
    class Meta(object):
        model = models.Project
        fields = ('project_id', 'project_name', 'owner', 'created_on', 'collaborators',
                  'description', 'current_stage', 'area_of_issues_open')


class IssueSerializer(serializer.ModelSerializer):
    class Meta(object):
        model = models.Issue
        fields = ('checkpoint_name', 'comments', 'created_by', 'created_on', 'description',
                  'is_resolved', 'project_id')


class IssueCommentSerializer(serializer.ModelSerializer):
    class Meta(object):
        model = models.IssueComment
        fields = ('comment_replies', 'comment_text', 'commenter', 'issue_id', 'likes',
                  'previous_edits', 'project_id', 'timestamp')


class IssueReplySerializer(serializer.ModelSerializer):
    class Meta(object):
        model = models.IssueReply
        fields = ('comment_id', 'reply_text', 'respondent', 'likes',
                  'previous_edits', 'timestamp')
