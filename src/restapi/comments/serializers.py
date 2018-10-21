from rest_framework import serializers as serializer
from djoser import serializers
from . import models


class CommentSerializer(serializer.ModelSerializer):
    class Meta(object):
        model = models.Comments
        fields = ('id', 'text', 'user', 'idea','likes',
                  'dislikes', 'commented_at')

class ReplySerializer(serializer.ModelSerializer):
    class Meta(object):
        model = models.Replies
        fields = ('id', 'text', 'comment', 'user', 'likes','dislikes',
                  'replied_at')