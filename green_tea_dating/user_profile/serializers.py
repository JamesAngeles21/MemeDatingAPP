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
		user = validated_data.pop('credentials', None)
		self.update_user(user)
		instance.save()
		return instance

	def update_user(self, user_data):
		user = get_user_model().objects(username=user_data['username'])
		UserSerializer.update(user, user_data)


	def create(self, validated_data):
		user = validated_data.pop('credentials', None)

		if not user:
			raise serializers.ValidationError(INVALID_DATA_ERR)

		if get_user_model().user_exists(user['email']):
			raise serializers.ValidationError(OBJECT_ALREADY_EXISTS_ERR) 

		validated_data['credentials'] = get_user_model().createUser(user)
		profile = UserProfile.objects.create(**validated_data)
		return profile
