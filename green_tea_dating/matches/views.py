from django.shortcuts import render, get_object_or_404
from matches.models import Matches
from matches.serializers import MatchSerializer
from rest_framework import status, permissions, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.
class MatchesViewSet(viewsets.ModelViewSet):
	queryset = UserProfile.objects.all()
	serializer_class = ProfileSerializer
	permission_classes = (permissions.AllowAny,)


