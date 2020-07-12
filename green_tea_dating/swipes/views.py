from django.shortcuts import render
from swipes.models import Swipe 
from swipes.serializers import SwipeSerializer
from user_profile.models import UserProfile
from rest_framework import status, permissions, viewsets
from rest_framework.response import Response 
from rest_framework.decorators import action

# Create your views here.
class SwipeViewSet(viewsets.ModelViewSet):
	queryset = Swipe.objects.all()
	serializer_class = SwipeSerializer
	permission_classes = (permissions.IsAuthenticated,)

	# updates entry if already exists 
	def create(self, request, *args, **kwargs):	
		profile = UserProfile.objects.get(pk=request.user)
		request.data['profile'] = profile
		entries = Swipe.objects.filter(profile=profile, content=request.data['content'])
		serializer = SwipeSerializer(data=request.data) if len(entries) == 0 else SwipeSerializer(entries[0], data=request.data) 

		if not serializer.is_valid():
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)

	@action(methods=['post'], detail=False)
	def batch_create(self, request, *args, **kwargs):
		swiped_content = request.data['swiped_content']
		profile = UserProfile.objects.get(pk=request.user)
		serialized_swipes = []

		for content in swiped_content:
			entries = Swipe.objects.filter(profile=profile, content=content['content'])
			data = {'profile': profile, 'content': content['content'], 'liked': content['liked']}
			serializer = SwipeSerializer(data=data) if len(entries) == 0 else SwipeSerializer(entries[0], data=data)

			if not serializer.is_valid():
				return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
			serialized_swipes.append(serializer)

		serialized_swipes = [serializer.save() for serializer in serialized_swipes]
		return Response(status=status.HTTP_201_CREATED)
