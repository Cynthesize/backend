from django.urls import path
from djoser import views as djoser_views
from rest_framework_jwt import views as jwt_views
from restAPI import views


urlpatterns = [
    path('api/view/', views.RestUserView.as_view(), name='user-view'),
    path('api/delete/', views.RestUserDeleteView.as_view(), name='user-delete'),
    path('api/logout/all/', views.RestUserLogoutAllView.as_view(), name='user-logout-all'),

    # Views are defined in Djoser, but we're assigning custom paths.
    path('api/register/', djoser_views.UserCreateView.as_view(), name='user-create'),

    # Views are defined in Rest Framework JWT, but we're assigning custom paths.
    path('api/login/', jwt_views.ObtainJSONWebToken.as_view(), name='user-login'),
    path('api/login/refresh/', jwt_views.RefreshJSONWebToken.as_view(), name='user-login-refresh'),
    path('api/add_idea/', views.AddIdeaView.as_view(), name='add-idea'),
]
