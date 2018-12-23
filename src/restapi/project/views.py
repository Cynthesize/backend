import uuid
from djoser.views import UserView, UserDeleteView
from djoser import serializers
from rest_framework import views, permissions, status, permissions, generics, filters
from rest_framework.response import Response
from . import models
from . import serializers
from .serializers import ProjectSerializer
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

    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.IssueSerializer
