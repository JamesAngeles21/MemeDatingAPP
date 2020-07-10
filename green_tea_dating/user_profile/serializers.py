from rest_framework import serializers
from django.contrib.auth import get_user_model
from users.serializers import UserSerializer
from user_profile.models import UserProfile
from ErrorMessages import INVALID_DATA_ERR, OBJECT_ALREADY_EXISTS_ERR

class ProfileSerializer(serializers.ModelSerializer):
	credentials = UserSerializer(required=True)

	class Meta:
		model = UserProfile
		fields = ('credentials', 'created_at', 'bio', 'occupation', 'birthday', 'twitter_handle', 'ig_handle')

	def update(self, instance, validated_data):
		instance.bio = validated_data.get('bio', instance.bio)
		instance.occupation = validated_data.get('occupation', instance.occupation)
		instance.twitter_handle = validated_data.get('twitter_handle', instance.twitter_handle)
		instance.ig_handle= validated_data.get('ig_handle', instance.ig_handle)

		instance.save()
		return instance

	def create(self, validated_data):
		user = validated_data.pop('credentials', None)

		if not user:
			raise serializers.ValidationError(INVALID_DATA_ERR)

		if get_user_model().user_exists(user['username']):
			raise serializers.ValidationError(OBJECT_ALREADY_EXISTS_ERR)

		validated_data['credentials'] = get_user_model().createUser(user)
		profile = UserProfile.objects.create(**validated_data)
		profile.save()
		return profile
