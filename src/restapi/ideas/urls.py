from django.urls import path
from djoser import views as djoser_views
from rest_framework_jwt import views as jwt_views
from ..ideas import views as views

urlpatterns = [
    path('', views.IdeaView.as_view(), name='api-add-idea'),
    path('vote/<int:idea_id>', views.update_upvotes, name='update-upvotes'),
    path('liked_ideas', views.UserUpvotedIdeasView.as_view(), name='api-liked-idea')
    path('pinned_ideas', views.UserPinnedIdeasView.as_view(), name='api-pinned-idea')
]
