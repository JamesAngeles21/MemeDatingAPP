from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.validators import UnicodeUsernameValidator


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = get_user_model()
		fields = ('username','email', 'password','first_name', 'last_name')
		extra_kwargs = {
			'username': {
				'validators': [UnicodeUsernameValidator()]
			},
			'email': {
				'validators': []
			},
			'password': {
				'write_only': True
			}
		}

	def update(instance, validated_data):
		instance.set_password(validated_data['password'])
		instance.save()
		return instance