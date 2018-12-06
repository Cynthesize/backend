from rest_framework import serializers as serializer
from djoser import serializers
from . import models


class ProjectSerializer(serializer.ModelSerializer):
    class Meta(object):
        model = models.Project
        fields = ('project_id', 'project_name', 'owner', 'created_on','collaborators',
                  'description', 'current_stage', 'area_of_issues_open')
