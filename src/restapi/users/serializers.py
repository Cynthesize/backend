from rest_framework import serializers as serializer
from djoser import serializers
from . import models


class UserSerializer(serializer.ModelSerializer):
    class Meta(object):
        model = models.User
        fields = (
            'bio',
            'birth_date',
            'email',
            'full_name',
            'username',
            'is_admin',
            'is_staff',
            'is_superuser',
            'location',
            'profile_pic',
            'social_links',
            'technologies',
            'website'
        )
