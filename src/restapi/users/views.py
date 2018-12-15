import uuid
from djoser.views import UserView, UserDeleteView
from djoser import serializers
from django.core import serializers as serializer
from rest_framework import views, permissions, status
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import permissions
from ..users.models import User
from ..ideas.models import Idea
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
        user_id = self.kwargs['username']
        queryset = User.objects.all()

        return queryset.filter(username=user_id)

    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer


class UserIdeaView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        ideas = Idea.objects.filter(owner = request.user.id) 
        data = serializer.serialize('json', ideas)

        return HttpResponse(data, content_type="application/json")

class UserAuthDeleteView(UserDeleteView):
    """
    Uses the default Djoser view, but add the IsOtpVerified permission.
    Use this endpoint to remove actually authenticated user.
    """
    serializer_class = serializers.UserDeleteSerializer
    permission_classes = [permissions.IsAuthenticated]