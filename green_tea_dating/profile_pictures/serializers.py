from rest_framework import serializers
from django.contrib.auth import get_user_model
from users.serializers import UserSerializer 
from profile_pictures.models import ProfilePicture
from user_profile.serializers import ProfileSerializer 
from ErrorMessages import INVALID_DATA_ERR

MAX_PROFILE_PICTURES = 5

class ProfilePictureListSerializer(serializers.ListSerializer):
	def validate(self, data):
		if len(data) == 0 or len(data) > MAX_PROFILE_PICTURES:
			raise serializers.ValidationError(INVALID_DATA_ERR)
		return data

	def create(self, validated_data):
		pictures = [ProfilePicture(**picture) for picture in validated_data]
		return ProfilePicture.objects.bulk_create(pictures)

class ProfilePictureSerializer(serializers.ModelSerializer):

	class Meta:
		model = ProfilePicture
		fields = ('user', 'path', 'picture_number')
		list_serializer_class = ProfilePictureListSerializer

	def create(self, validated_data):
		profile_picture = ProfilePicture.objects.create(**validated_data)
		profile_picture.save()
		return profile_picture


