import uuid
from djoser.views import UserView, UserDeleteView
from djoser import serializers
from rest_framework import views, permissions, status, permissions, generics, filters
from rest_framework.response import Response
from . import models
from . import serializers
from rest_framework.decorators import api_view


class ProjectView(generics.ListCreateAPIView):
    """Use this endpoint to add projects in the backend."""

    def get_queryset(self):
        queryset = models.Project.objects.all()
        project_id = self.request.query_params.get('id', None)

        if project_id is None:
            return queryset
        else:
            return queryset.filter(id=project_id)

    def put(self, request):
        update_reference = self.request.data['update_reference']
        project_id = self.request.data['project_id']
        new_value = self.request.data['new_value']

        project = models.Project.objects.get(project_id=project_id)

        serializer = serializers.ProjectSerializer(
            project, data={update_reference: new_value}, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.ProjectSerializer


class IssueView(generics.ListCreateAPIView):
    """Use this endpoint to add projects in the backend."""

    def get_queryset(self):
        queryset = models.Issue.objects.all()
        issue_id = self.request.query_params.get('id', None)

        if issue_id is None:
            return queryset
        else:
            return queryset.filter(id=issue_id)

    def put(self, request):
        update_reference = self.request.data['update_reference']
        issue_id = self.request.data['issue_id']
        new_value = self.request.data['new_value']

        issue = models.Issue.objects.get(id=issue_id)

        serializer = serializers.IssueSerializer(
            issue, data={update_reference: new_value}, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.IssueSerializer


class IssueCommentView(generics.ListCreateAPIView):
    """Use this endpoint to add issue comments in the backend."""

    def get_queryset(self):
        queryset = models.IssueComment.objects.all()
        comment_id = self.request.query_params.get('id', None)

        if comment_id is None:
            return queryset
        else:
            return queryset.filter(id=comment_id)

    def put(self, request):
        update_reference = self.request.data['update_reference']
        comment_id = self.request.data['comment_id']
        new_value = self.request.data['new_value']

        issue_comment = models.IssueComment.objects.get(id=comment_id)

        serializer = serializers.IssueCommentSerializer(
            issue_comment, data={update_reference: new_value}, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.IssueCommentSerializer


class IssueReplyView(generics.ListCreateAPIView):
    """Use this endpoint to add projects in the backend."""

    def get_queryset(self):
        queryset = models.IssueReply.objects.all()
        reply_id = self.request.query_params.get('id', None)

        if reply_id is None:
            return queryset
        else:
            return queryset.filter(id=reply_id)

    def put(self, request):
        update_reference = self.request.data['update_reference']
        reply_id = self.request.data['reply_id']
        new_value = self.request.data['new_value']

        issue_reply = models.IssueReply.objects.get(id=reply_id)

        serializer = serializers.IssueReplySerializer(
            issue_reply, data={update_reference: new_value}, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.IssueReplySerializer
