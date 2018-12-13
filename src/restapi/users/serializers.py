from rest_framework import serializers as serializer
from djoser import serializers
from . import models


class UserSerializer(serializer.ModelSerializer):
    class Meta(object):
        model = models.User
        fields = ('username', 'full_name', 'email', 'is_admin', 'is_staff',	'is_superuser', 'birth_date', 'technologies', 'bio', 'social_links')
