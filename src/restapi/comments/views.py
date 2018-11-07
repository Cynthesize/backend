import uuid
from . import models
from .serializers import CommentSerializer, ReplySerializer
from ..comments.models import Comments, Replies
from djoser.views import UserView, UserDeleteView
from rest_framework import views, permissions, status, generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

class RetrieveCommentView(generics.RetrieveAPIView):
    """Use this endpoint to add ideas in the backend."""
    def get_queryset(self):
        queryset = Comments.objects.all()
        return queryset

    def retrieve(self, *args, **kwargs):
        comment_object = {}
        idea = models.Idea.objects.get(pk = kwargs['idea_id'])
        comment_list = idea.comments_set.filter(idea=idea)
        for comment in comment_list:
            replies_list = comment.replies_set.filter(comment=comment)
            comment_object[comment.text] = []
            for replies in replies_list:
                comment_object[comment.text].append(replies.text)
        return Response(comment_object, status.HTTP_201_CREATED)

    permission_classes = [permissions.AllowAny]
    serializer_class = CommentSerializer

class CommentView(generics.ListCreateAPIView):
    """Use this endpoint to add ideas in the backend."""
    def get_queryset(self):
        queryset = Comments.objects.all()
        return queryset.filter(idea=self.request.query_params.get('idea_id', None))

    permission_classes = [permissions.AllowAny]
    serializer_class = CommentSerializer

class ReplyView(generics.ListCreateAPIView):
    """Use this endpoint to add ideas in the backend."""
    def get_queryset(self):
        queryset = Replies.objects.all()
        return queryset

    permission_classes = [permissions.AllowAny]
    serializer_class = ReplySerializer