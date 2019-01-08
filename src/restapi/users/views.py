import uuid
import datetime
from djoser.views import UserView, UserDeleteView
from djoser import serializers
from django.core import serializers as serializer
from rest_framework import views, permissions, status
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import permissions
from ..users.models import User
from ..ideas.models import Idea
from ..project.models import Project
from .serializers import UserSerializer
from rest_framework import generics
from pprint import pprint
from rest_framework.decorators import api_view


class UserLogoutAllView(views.APIView):
    """
    Use this endpoint to log out all sessions for a given user.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        user.jwt_secret = uuid.uuid4()
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserAuthView(generics.ListCreateAPIView):
    def get_queryset(self):
        username = self.request.query_params.get('username', None)
        queryset = User.objects.all()

        return queryset.filter(username=username)

    def put(self, request):
        bio = self.request.data['bio']
        technologies = self.request.data['technologies'].split(',')[:-1]
        birth_date = self.request.data['birth_date']
        location = self.request.data['location']
        username = self.request.data['username']
        website = self.request.data['website']

        try:
            User.objects.filter(username=username).update(
                bio=bio, technologies=technologies, birth_date=birth_date, location=location,
                website=website)
            return Response(status.HTTP_201_CREATED)
        except:
            return Response(status.HTTP_400_BAD_REQUEST)

    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer


class UserIdeaView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        ideas = Idea.objects.filter(owner=request.user.id)
        data = serializer.serialize('json', ideas)

        return HttpResponse(data, content_type="application/json")


class UserAuthDeleteView(UserDeleteView):
    """
    Uses the default Djoser view, but add the IsOtpVerified permission.
    Use this endpoint to remove actually authenticated user.
    """
    serializer_class = serializers.UserDeleteSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserContributionsView(views.APIView):
    """Use this endpoint to return users' contribution across various
    categories.
    """
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        try:
            username = self.request.query_params.get('username')
            user = User.objects.get(username=username)
            ideas = Idea.objects.filter(owner=user.id)
            projects = Project.objects.filter(owner=user.id)
            response_object = {
                'project_list': [],
                'idea_list': []
            }
            if projects:
                for project in projects:
                    response_object['project_list'].append(project.to_short_dict())
            if ideas:
                for idea in ideas:
                    response_object['idea_list'].append(idea.to_short_dict())
            return Response(response_object)
        except:
            return Response(status.HTTP_400_BAD_REQUEST)
