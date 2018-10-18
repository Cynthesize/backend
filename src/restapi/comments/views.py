import uuid
from djoser.views import UserView, UserDeleteView
from djoser import serializers
from rest_framework import views, permissions, status
from rest_framework.response import Response
from rest_framework import permissions
from ..comments.models import Comments, Replies
from rest_framework import generics
from .serializers import CommentSerializer, ReplySerializer
from pprint import pprint
from rest_framework.decorators import api_view

class CommentView(generics.ListCreateAPIView):
    """Use this endpoint to add ideas in the backend."""
    def get_queryset(self):
        queryset = Comments.objects.all()
        return queryset

    permission_classes = [permissions.AllowAny]
    serializer_class = CommentSerializer

class ReplyView(generics.ListCreateAPIView):
    """Use this endpoint to add ideas in the backend."""
    def get_queryset(self):
        queryset = Replies.objects.all()
        return queryset

    permission_classes = [permissions.AllowAny]
    serializer_class = ReplySerializer