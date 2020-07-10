from user_profile.models import UserProfile
from user_profile.serializers import ProfileSerializer 
from django.shortcuts import render, get_object_or_404
from rest_framework import status, permissions, viewsets
from rest_framework.response import Response 
from rest_framework.decorators import action
from django.contrib.auth import get_user_model
from django.forms.models import model_to_dict 

# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
	queryset = UserProfile.objects.all()
	serializer_class = ProfileSerializer
	permission_classes = (permissions.AllowAny,)


	def retrieve(self, request, pk=None):
		profile = get_object_or_404(UserProfile, pk=pk)
		serializer = ProfileSerializer(profile)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def create(self, request, *args, **kwargs):
		serializer = ProfileSerializer(data=request.data)
		if not serializer.is_valid():
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)

	def partial_update(self, request, pk=None, *args, **kwargs):
		profile = get_object_or_404(UserProfile, pk=pk) 
		serializer = ProfileSerializer(profile, request.data, partial=True)
		if not serializer.is_valid():
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		serializer.save()
		return Response(serializer.data, status=status.HTTP_200_OK)

	def destroy(self, request, pk=None, *args, **kwargs):
		profile = get_object_or_404(UserProfile, pk=pk)
		user = get_user_model().objects.get(username=profile.credentials.username)
		user.delete()
		self.perform_destroy(profile)
		return Response(status=status.HTTP_204_NO_CONTENT)