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
from user_profile.views import UserProfileViewSet
from content.views import ContentViewSet
from swipes.views import SwipeViewSet
from conversations.views import ConversationsViewSet

router = routers.DefaultRouter(trailing_slash=True)
router.register(r'profile', UserProfileViewSet, basename='profile')
router.register(r'content', ContentViewSet, basename='content')
router.register(r'swipe', SwipeViewSet, basename='swipe')
router.register(r'conversations', ConversationsViewSet, basename='conversations')

urlpatterns = [
	path('', include(router.urls)),
]
