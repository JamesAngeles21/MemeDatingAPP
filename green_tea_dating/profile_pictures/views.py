from profile_pictures.models import ProfilePicture
from profile_pictures.serializers import ProfilePictureSerializer
from django.shortcuts import render, get_object_or_404
from rest_framework import status, permissions, viewsets
from rest_framework.response import Response 
from rest_framework.decorators import action
from django.contrib.auth import get_user_model
from django.forms.models import model_to_dict 

# Create your views here.
class ProfilePictureViewSet(viewsets.ModelViewSet):
	queryset = ProfilePicture.objects.all()
	serializers_class = ProfilePictureSerializer
	permission_classes = (permissions.IsAuthenticated,)

	def create(self, request, *args, **kwargs):
		for picture in request.data:
			picture['user'] = request.user  

		ProfilePicture.objects.filter(user=request.user).delete()
		serializer = ProfilePictureSerializer(data=request.data, many=True, allow_empty=False)
		if not serializer.is_valid():
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)


	@action(detail=False, methods=['get'])
	def get_profile_pictures(self, request, *args, **kwargs):
		pictures = ProfilePicture.objects.filter(user=request.user).order_by('picture_number')
		serializer = ProfilePictureSerializer(pictures, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)


