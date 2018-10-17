import uuid
from djoser.views import UserView, UserDeleteView
from djoser import serializers
from rest_framework import views, permissions, status
from rest_framework.response import Response
from rest_framework import permissions
from ..ideas.models import Idea, User
from ..ideas.serializers import serializers as srl
from rest_framework import generics
from .serializers import IdeaSerializer
from pprint import pprint
from rest_framework.decorators import api_view

class AddIdeaView(generics.ListCreateAPIView):
    """Use this endpoint to add ideas in the backend."""
    def get_queryset(self):
        queryset = Idea.objects.all()
        return queryset

    permission_classes = [permissions.AllowAny]
    serializer_class = IdeaSerializer

@api_view(['PUT'])
def update_upvotes(request, idea_id):
    idea = Idea.objects.get(pk = idea_id)
    user = User.objects.get(pk = request.user.id)
    is_idea_upvoted = user.upvoted_ideas.filter(idea_id=idea_id)
    upvotes = idea.upvotes

    if is_idea_upvoted:
        upvotes -= 1
        user.upvoted_ideas.filter(idea_id=idea_id).delete()
    else:
        upvotes += 1
        user.upvoted_ideas.create(idea=idea, user=user)   
    serializer = IdeaSerializer(idea, data = {'upvotes': upvotes}, partial = True)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST) 
