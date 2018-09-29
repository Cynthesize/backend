import uuid
from djoser.views import UserView, UserDeleteView
from djoser import serializers
from rest_framework import views, permissions, status
from rest_framework.response import Response
from rest_framework import permissions
from restAPI.models import RestUser, Idea
from restAPI import serializers as srl


class RestUserLogoutAllView(views.APIView):
    """
    Use this endpoint to log out all sessions for a given user.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        user.jwt_secret = uuid.uuid4()
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RestUserView(UserView):
    """
    Uses the default Djoser view, but add the IsOtpVerified permission.
    Use this endpoint to retrieve/update user.
    """
    model = RestUser
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]
 

class RestUserDeleteView(UserDeleteView):
    """
    Uses the default Djoser view, but add the IsOtpVerified permission.
    Use this endpoint to remove actually authenticated user.
    """
    serializer_class = serializers.UserDeleteSerializer
    permission_classes = [permissions.IsAuthenticated]


class RestAddIdeaView(views.APIView):
    """Use this endpoint to add ideas in the backend."""
    model = Idea
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = [srl.IdeaSerializer]
