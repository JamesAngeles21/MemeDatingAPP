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


	@action(detail=False, methods=['get'])
	def get_profile(self, request, *args, **kwargs):
		profile = UserProfile.objects.get(pk=request.user.email)
		serializer = ProfileSerializer(profile).data
		if not serializer.is_valid():
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		return Response(serializer,status=status.HTTP_200_OK)

	def create(self, request, *args, **kwargs):
		serializer = ProfileSerializer(data=request.data)
		if not serializer.is_valid():
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)

	@action(detail=False, methods=['delete'])
	def delete(self, request,*args, **kwargs):
		profile = get_object_or_404(UserProfile, pk=request.data['email']) 
		user = get_user_model().objects.get(email=profile.credentials.email)
		user.delete()
		self.perform_destroy(profile)
		return Response(status=status.HTTP_204_NO_CONTENT)