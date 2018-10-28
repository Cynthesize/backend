import uuid
from djoser.views import UserView, UserDeleteView
from djoser import serializers
from rest_framework import views, permissions, status, permissions, generics, filters
from rest_framework.response import Response
from . import models
from . import serializers
from .serializers import IdeaSerializer
from rest_framework.decorators import api_view

class IdeaView(generics.ListCreateAPIView):
    """Use this endpoint to add ideas in the backend."""
    def get_queryset(self):
        queryset = models.Idea.objects.all()
        idea_id = self.request.query_params.get('id', None)
        idea_cursor = self.request.query_params.get('idea_cursor', None)

        if idea_id is None:
            if idea_cursor is None:
                return queryset
            else:
                return queryset[int(idea_cursor):int(idea_cursor)+5]
        else:
            return queryset.filter(id=idea_id)

    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.IdeaSerializer


class UpvotesView(views.APIView):
    permission_classes = [permissions.AllowAny]
    def put(self, request, idea_id):
        idea = models.Idea.objects.get(pk = idea_id)
        user = models.User.objects.get(pk = request.user.id)
        user_upvoted_ideas = user.upvoted_ideas.get_or_create(user=request.user.id)[0]

        upvotes = idea.upvotes

        if str(idea_id) in user_upvoted_ideas.idea_list:
            upvotes -= 1
            user_upvoted_ideas.idea_list.remove(str(idea_id))
            user.upvoted_ideas.update(idea_list=user_upvoted_ideas.idea_list)
        else:
            upvotes += 1
            user_upvoted_ideas.idea_list.append(str(idea_id))
            user.upvoted_ideas.update(idea_list=user_upvoted_ideas.idea_list)

        serializer = IdeaSerializer(idea, data = {'upvotes': upvotes}, partial = True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class UserUpvotedIdeasView(generics.ListCreateAPIView):
    """Use this endpoint to fetch upvoted ideas from the backend."""

    def get_queryset(self):
        queryset = models.Upvoted_ideas.objects.all()
        return queryset
    model = models.Upvoted_ideas
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.UserUpvotedIdeasSerializer


class UserPinnedIdeasView(generics.ListCreateAPIView):
    """Use this endpoint to fetch upvoted ideas from the backend."""

    def get_queryset(self):
        queryset = models.Pinned_ideas.objects.all()
        return queryset
    model = models.Pinned_ideas
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.UserUpvotedIdeasSerializer
