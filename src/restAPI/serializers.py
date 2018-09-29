from rest_framework import serializers as srl
from djoser import serializers
from . import models


class IdeaSerializer(srl.ModelSerializer):
    class Meta(object):
        model = models.Idea
        fields = ('id', 'idea_name', 'owner', 'created_on',
                  'description', 'likes')
