from django.urls import path
from djoser import views as djoser_views
from rest_framework_jwt import views as jwt_views
from ..comments import views

urlpatterns = [
    path('', views.CommentView.as_view()),
    path('reply', views.ReplyView.as_view())
]
