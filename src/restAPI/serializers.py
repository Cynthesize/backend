from rest_framework import serializers as srl
from djoser import serializers
from . import models

 
class UserSerializer(serializers.UserSerializer):
    class Meta(object):
        model = models.RestUser
        fields = ('id', 'email', 'full_name',
                  'date_joined', 'password', 'username')
        extra_kwargs = {'password': {'write_only': True}}


class IdeaSerializer(srl.ModelSerializer):
    class Meta(object):
        model = models.Idea
        fields = ('id', 'idea_name', 'owner', 'created_on',
                  'description', 'likes')
