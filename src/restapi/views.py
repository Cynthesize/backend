import uuid
from djoser.views import UserView, UserDeleteView
from djoser import serializers
from rest_framework import views, permissions, status
from rest_framework.response import Response
from rest_framework import permissions
from restapi.models import User, Idea
from restapi import serializers as srl
from rest_framework import generics
from .serializers import IdeaSerializer
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


class UserAuthView(UserView):
    """
    Uses the default Djoser view, but add the IsOtpVerified permission.
    Use this endpoint to retrieve/update user.
    """
    model = User
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]
 

class UserAuthDeleteView(UserDeleteView):
    """
    Uses the default Djoser view, but add the IsOtpVerified permission.
    Use this endpoint to remove actually authenticated user.
    """
    serializer_class = serializers.UserDeleteSerializer
    permission_classes = [permissions.IsAuthenticated]


class AddIdeaView(generics.ListCreateAPIView):
    """Use this endpoint to add ideas in the backend."""
    def get_queryset(self):
        page = int(self.request.GET['page'])
        queryset = Idea.objects.all()[page:(page+5)]
        return queryset

    permission_classes = [permissions.AllowAny]
    serializer_class = IdeaSerializer

@api_view(['PUT'])
def update_upvotes(request, idea_id):
    idea = Idea.objects.get(pk = idea_id)
    user = User.objects.get(pk = request.user.id)
    upvotes = idea.upvoted_ideas
    
    if idea in user.upvoted_ideas.all():
        upvotes -= 1
        user.upvoted_ideas.remove(idea)
    else:
        upvotes += 1
        user.upvoted_ideas.add(idea)    
    serializer = IdeaSerializer(idea, data = {'upvotes': upvotes}, partial = True)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST) 
