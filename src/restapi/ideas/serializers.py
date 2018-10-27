from rest_framework import serializers as serializer
from djoser import serializers
from . import models


class IdeaSerializer(serializer.ModelSerializer):
    class Meta(object):
        model = models.Idea
        fields = ('id', 'idea_name', 'owner', 'created_on','require_assistance',
                  'description', 'upvotes')

class UserUpvotedIdeasSerializer(serializer.ModelSerializer):
    class Meta(object):
        model = models.Upvoted_ideas
        fields = ('user', 'idea')
