"""green_tea_dating URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token
from user_profile.views import UserProfileViewSet
from content.views import ContentViewSet
from swipes.views import SwipeViewSet
from conversations.views import ConversationsViewSet
from matches.views import MatchesViewSet
from potential_matches.views import PotentialMatchesViewSet
from swiped_users.views import SwipedUsersViewSet

router = routers.DefaultRouter(trailing_slash=True)
router.register(r'profile', UserProfileViewSet, basename='profile')
router.register(r'content', ContentViewSet, basename='content')
router.register(r'swipe', SwipeViewSet, basename='swipe')
router.register(r'conversations', ConversationsViewSet, basename='conversations')
router.register(r'matches', MatchesViewSet, basename='matches')
router.register(r'potential_matches', PotentialMatchesViewSet, basename='potential_matches')
router.register(r'swiped_users', SwipedUsersViewSet, basename='swiped_users')


urlpatterns = [
	path('', include(router.urls)),
	path('token-auth/', obtain_jwt_token),
	path('token-verify/', verify_jwt_token),
	path('token-refresh/', refresh_jwt_token),
]
